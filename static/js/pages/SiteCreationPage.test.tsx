import sinon, { SinonStub } from "sinon"
import { act } from "react-dom/test-utils"

import SiteCreationPage from "./SiteCreationPage"
import IntegrationTestHelper, {
  TestRenderer
} from "../util/integration_test_helper_old"
import {
  makeWebsiteDetail,
  makeWebsiteStarter
} from "../util/factories/websites"
import { siteDetailUrl, siteApi, startersApi } from "../lib/urls"

import { Website, WebsiteStarter } from "../types/websites"
import { assertNotNil } from "../test_util"
import { ReactWrapper } from "enzyme"
import { SiteForm, SiteFormProps } from "../components/forms/SiteForm"
import { FormikHelpers } from "formik"

const simulateSubmit = (
  wrapper: ReactWrapper<SiteFormProps>,
  formikStubs: Partial<Record<keyof FormikHelpers<any>, jest.Mock>>,
  data: any
) => {
  const onSubmit = wrapper.prop("onSubmit")
  assertNotNil(onSubmit)
  return act(async () => {
    // @ts-expect-error using Partial on FormikHelpers... we don't need all of them
    onSubmit(data, formikStubs)
  })
}

describe("SiteCreationPage", () => {
  let helper: IntegrationTestHelper,
    render: TestRenderer,
    starters: Array<WebsiteStarter>,
    website: Website,
    historyPushStub: jest.Mock

  beforeEach(() => {
    helper = new IntegrationTestHelper()
    starters = [makeWebsiteStarter(), makeWebsiteStarter()]
    website = makeWebsiteDetail()
    historyPushStub = jest.fn()
    render = helper.configureRenderer(SiteCreationPage, {
      history:  { push: historyPushStub },
      entities: {
        starters: []
      },
      queries: {}
    })

    helper.mockGetRequest(startersApi.toString(), starters)
  })

  afterEach(() => {
    helper.cleanup()
  })

  it("renders a form with the right props", async () => {
    const { wrapper } = await render()
    const form = wrapper.find("SiteForm")
    expect(form.exists()).toBe(true)
    expect(form.prop("websiteStarters")).toBe(starters)
  })

  it("sets the page title", async () => {
    const { wrapper } = await render()
    expect(wrapper.find("DocumentTitle").prop("title")).toBe(
      "OCW Studio | New Site"
    )
  })

  describe("passes a form submit function", () => {
    const errorMsg = "Error"
    let formikStubs: { [key: string]: jest.Mock }, createWebsiteStub: SinonStub

    beforeEach(() => {
      formikStubs = {
        setErrors:     jest.fn(),
        setSubmitting: jest.fn(),
        setStatus:     jest.fn()
      }
    })

    it("that creates a new site and redirect on success", async () => {
      createWebsiteStub = helper.mockPostRequest(siteApi.toString(), website)
      const { wrapper } = await render()
      const form = wrapper.find(SiteForm)
      await simulateSubmit(form, formikStubs, {
        title:    "My Title",
        short_id: "My-Title",
        starter:  1
      })
      sinon.assert.calledOnce(createWebsiteStub)
      expect(formikStubs.setSubmitting).toHaveBeenCalledTimes(1)
      expect(formikStubs.setSubmitting).toHaveBeenCalledWith(false)
      expect(historyPushStub).toHaveBeenCalledTimes(1)
      expect(historyPushStub).toHaveBeenCalledWith(
        siteDetailUrl.param({ name: website.name }).toString()
      )
    })

    it("that sets form errors if the API request fails", async () => {
      const errorResp = {
        errors: {
          title: errorMsg
        }
      }
      createWebsiteStub = helper.mockPostRequest(
        siteApi.toString(),
        errorResp,
        400
      )
      const { wrapper } = await render()
      const form = wrapper.find(SiteForm)
      await simulateSubmit(form, formikStubs, {
        title:    errorMsg,
        short_id: "my-site",
        starter:  1
      })
      sinon.assert.calledOnce(createWebsiteStub)
      expect(formikStubs.setErrors).toHaveBeenCalledTimes(1)
      expect(formikStubs.setErrors).toHaveBeenCalledWith({
        ...errorResp.errors,
        short_id: undefined,
        starter:  undefined
      })
      expect(historyPushStub).not.toHaveBeenCalled()
    })

    it("that sets a status if the API request fails with a string error message", async () => {
      const errorResp = {
        errors: errorMsg
      }
      createWebsiteStub = helper.mockPostRequest(
        siteApi.toString(),
        errorResp,
        400
      )
      const { wrapper } = await render()
      const form = wrapper.find(SiteForm)
      await simulateSubmit(form, formikStubs, {
        title:    "My Title",
        short_id: "My-Title",
        starter:  1
      })
      sinon.assert.calledOnce(createWebsiteStub)
      expect(formikStubs.setStatus).toHaveBeenCalledTimes(1)
      expect(formikStubs.setStatus).toHaveBeenCalledWith(errorMsg)
      expect(historyPushStub).not.toHaveBeenCalled()
    })
  })
})
