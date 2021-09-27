import React, {
  MouseEvent as ReactMouseEvent,
  useCallback,
  useState
} from "react"
import { useLocation } from "react-router-dom"
import { useMutation, useRequest } from "redux-query-react"
import { useSelector } from "react-redux"

import SiteContentEditor from "./SiteContentEditor"
import PaginationControls from "./PaginationControls"
import Card from "./Card"
import BasicModal from "./BasicModal"
import { useWebsite } from "../context/Website"

import { WEBSITE_CONTENT_PAGE_SIZE } from "../constants"
import { siteContentListingUrl } from "../lib/urls"
import { splitFieldsIntoColumns } from "../lib/site_content"
import {
  syncWebsiteContentMutation,
  websiteContentListingRequest,
  WebsiteContentListingResponse
} from "../query-configs/websites"
import { getWebsiteContentListingCursor } from "../selectors/websites"

import {
  ContentListingParams,
  RepeatableConfigItem,
  WebsiteContentListItem,
  WebsiteContentModalState
} from "../types/websites"
import { createModalState } from "../types/modal_state"

export default function RepeatableContentListing(props: {
  configItem: RepeatableConfigItem
}): JSX.Element | null {
  const { configItem } = props

  const website = useWebsite()

  const { search } = useLocation()
  const offset = Number(new URLSearchParams(search).get("offset") ?? 0)

  const listingParams: ContentListingParams = {
    name: website.name,
    type: configItem.name,
    offset
  }
  const [
    { isPending: contentListingPending },
    fetchWebsiteContentListing
  ] = useRequest(websiteContentListingRequest(listingParams, false, false))
  const listing: WebsiteContentListingResponse = useSelector(
    getWebsiteContentListingCursor
  )(listingParams)
  const [{ isPending: syncIsPending }, syncWebsiteContent] = useMutation(() =>
    syncWebsiteContentMutation(website.name)
  )

  const [drawerState, setDrawerState] = useState<WebsiteContentModalState>(
    createModalState("closed")
  )
  const [syncModalState, setSyncModalState] = useState({
    message:   "",
    isVisible: false
  })
  const toggleSyncModal = (message: string) =>
    setSyncModalState({
      message:   message,
      isVisible: !syncModalState.isVisible
    })

  const closeContentDrawer = useCallback(() => {
    setDrawerState(createModalState("closed"))
  }, [setDrawerState])

  if (contentListingPending) {
    return <div className="site-page container">Loading...</div>
  }
  if (!listing) {
    return null
  }

  const startAddOrEdit = (textId: string | null) => (
    event: ReactMouseEvent<HTMLLIElement | HTMLAnchorElement, MouseEvent>
  ) => {
    event.preventDefault()

    setDrawerState(
      textId ? createModalState("editing", textId) : createModalState("adding")
    )
  }

  const labelSingular = configItem.label_singular ?? configItem.label

  const modalTitle = `${
    drawerState.editing() ? "Edit" : "Add"
  } ${labelSingular}`

  const modalClassName = `right ${
    splitFieldsIntoColumns(configItem.fields).length > 1 ? "wide" : ""
  }`

  const onSubmitContentSync = async (
    event: ReactMouseEvent<HTMLLIElement | HTMLAnchorElement, MouseEvent>
  ) => {
    event.preventDefault()
    if (syncIsPending) {
      return
    }
    const response = await syncWebsiteContent()
    const successMsg =
      "Resources are being synced with Google Drive. Please revisit this page in a few minutes."
    const failMsg =
      "Something went wrong syncing with Google Drive.  Please try again or contact support."
    toggleSyncModal(!response || response.status !== 200 ? failMsg : successMsg)
  }

  return (
    <>
      <BasicModal
        isVisible={drawerState.open()}
        hideModal={closeContentDrawer}
        title={modalTitle}
        className={modalClassName}
      >
        {modalProps =>
          drawerState.open() ? (
            <div className="m-3">
              <SiteContentEditor
                loadContent={true}
                configItem={configItem}
                editorState={drawerState}
                hideModal={modalProps.hideModal}
                fetchWebsiteContentListing={fetchWebsiteContentListing}
              />
            </div>
          ) : null
        }
      </BasicModal>
      <BasicModal
        isVisible={syncModalState.isVisible}
        hideModal={() => toggleSyncModal("")}
        title="Syncing with Google Drive"
        className={null}
      >
        {_ =>
          syncModalState ? (
            <div className="m-3">{syncModalState.message}</div>
          ) : null
        }
      </BasicModal>
      <div>
        <Card>
          <div className="d-flex flex-direction-row align-items-right justify-content-between pb-1Z">
            <h3>{configItem.label}</h3>
            <div>
              <a className="btn blue-button add" onClick={startAddOrEdit(null)}>
                Add {labelSingular}
              </a>
              {SETTINGS.gdrive_enabled ? (
                <a
                  className="btn blue-button sync ml-2"
                  onClick={onSubmitContentSync}
                >
                  Sync w/Google Drive
                </a>
              ) : null}
            </div>
          </div>
          <ul className="ruled-list">
            {listing.results.map((item: WebsiteContentListItem) => (
              <li
                key={item.text_id}
                className="py-3 listing-result"
                onClick={startAddOrEdit(item.text_id)}
              >
                <div className="d-flex flex-direction-row align-items-center justify-content-between">
                  <span>{item.title}</span>
                </div>
              </li>
            ))}
          </ul>
        </Card>
      </div>
      <PaginationControls
        listing={listing}
        previous={siteContentListingUrl
          .param({
            name:        website.name,
            contentType: configItem.name
          })
          .query({ offset: offset - WEBSITE_CONTENT_PAGE_SIZE })
          .toString()}
        next={siteContentListingUrl
          .param({
            name:        website.name,
            contentType: configItem.name
          })
          .query({ offset: offset + WEBSITE_CONTENT_PAGE_SIZE })
          .toString()}
      />
    </>
  )
}
