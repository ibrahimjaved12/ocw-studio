import {
  sitesBaseUrl,
  newSiteUrl,
  siteDetailUrl,
  siteContentListingUrl,
  siteCollaboratorsUrl,
  siteCollaboratorsAddUrl,
  siteCollaboratorsDetailUrl,
  siteApi,
  siteApiDetailUrl,
  siteApiListingUrl,
  siteApiCollaboratorsUrl,
  siteApiCollaboratorsDetailUrl,
  siteApiContentUrl,
  siteApiContentDetailUrl,
  siteApiContentListingUrl,
  collectionsApiUrl,
  collectionsApiDetailUrl,
  wcItemsApiUrl,
  wcItemsApiDetailUrl,
  collectionsBaseUrl
} from "./urls"

describe("urls", () => {
  describe("Page URLs", () => {
    describe("Site URLs", () => {
      [
        [10, "/sites/?offset=10"],
        [20, "/sites/?offset=20"]
      ].forEach(([offset, expectedLink]) => {
        it(`renders a URL for the site dashboard with offset=${offset}`, () => {
          expect(sitesBaseUrl.query({ offset }).toString()).toBe(expectedLink)
        })
      })

      it("returns a basic URL for the site dashboard", () => {
        expect(sitesBaseUrl.toString()).toBe("/sites/")
      })

      it("makes a URL for creating new sites", () => {
        expect(newSiteUrl.toString()).toBe("/new-site/")
      })

      it("renders a site URL", () => {
        expect(siteDetailUrl.param({ name: "site-name" }).toString()).toBe(
          "/sites/site-name/"
        )
      })

      it("renders a site listing URL", () => {
        expect(
          siteContentListingUrl
            .param({ name: "site-name", contentType: "resource" })
            .toString()
        ).toBe("/sites/site-name/type/resource/")
      })

      it("renders a URL for collaborators", () => {
        expect(
          siteCollaboratorsUrl.param({ name: "site-name" }).toString()
        ).toBe("/sites/site-name/collaborators/")
      })

      it("renders a URL for adding collaborators", () => {
        expect(
          siteCollaboratorsAddUrl.param({ name: "site-name" }).toString()
        ).toBe("/sites/site-name/collaborators/new/")
      })

      it("renders a URL for collaborators detail", () => {
        expect(
          siteCollaboratorsDetailUrl
            .param({ name: "site-name", userId: 1 })
            .toString()
        ).toBe("/sites/site-name/collaborators/1/")
      })
    })

    //
    ;[
      [0, "/collections/?offset=0"],
      [10, "/collections/?offset=10"],
      [20, "/collections/?offset=20"]
    ].forEach(([offset, expectedLink]) => {
      it(`renders a collection URL with offset=${offset}`, () => {
        expect(collectionsBaseUrl.query({ offset }).toString()).toBe(
          expectedLink
        )
      })
    })
  })

  describe("apis", () => {
    describe("Website APIs", () => {
      it("renders a top-level site API", () => {
        expect(siteApi.toString()).toBe("/api/websites/")
      })

      it("renders a URL for site listing", () => {
        expect(siteApiListingUrl.query({ offset: 20 }).toString()).toBe(
          "/api/websites/?limit=10&offset=20"
        )
      })

      it("renders a URL for site detail", () => {
        expect(siteApiDetailUrl.param({ name: "site-name" }).toString()).toBe(
          "/api/websites/site-name/"
        )
      })

      it("renders a URL for site collaborators", () => {
        expect(
          siteApiCollaboratorsUrl.param({ name: "site-name" }).toString()
        ).toBe("/api/websites/site-name/collaborators/")
      })

      it("renders a collaborator detail URL", () => {
        expect(
          siteApiCollaboratorsDetailUrl
            .param({
              name:   "site-name",
              userId: 1
            })
            .toString()
        ).toBe("/api/websites/site-name/collaborators/1/")
      })

      it("renders a URL for site content listing", () => {
        expect(siteApiContentUrl.param({ name: "site-name" }).toString()).toBe(
          "/api/websites/site-name/content/"
        )
      })

      it("renders a URL for site content detail", () => {
        expect(
          siteApiContentDetailUrl
            .param({ name: "site-name", textId: "my-text-id" })
            .toString()
        ).toBe("/api/websites/site-name/content/my-text-id/")
      })

      it("should render a content listing URL", () => {
        expect(
          siteApiContentListingUrl
            .param({ name: "the-best-course" })
            .query({ offset: 40 })
            .toString()
        ).toBe("/api/websites/the-best-course/content/?limit=10&offset=40")
      })
    })

    describe("Collections APIs", () => {
      it("renders the collections API url", () => {
        expect(collectionsApiUrl.toString()).toBe("/api/collections/")
      })

      it("renders a collection detail API url", () => {
        expect(
          collectionsApiDetailUrl.param({ collectionId: 4 }).toString()
        ).toBe("/api/collections/4/")
      })

      it("renders collection items list API url", () => {
        expect(wcItemsApiUrl.param({ collectionId: 4 }).toString()).toBe(
          "/api/collections/4/items/"
        )
      })

      it("renders collection item detail API url", () => {
        expect(
          wcItemsApiDetailUrl.param({ collectionId: 4, itemId: 3 }).toString()
        ).toBe("/api/collections/4/items/3/")
      })
    })
  })
})
