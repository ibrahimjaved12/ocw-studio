Release Notes
=============

Version 0.84.1 (Released January 23, 2023)
--------------

- Resource links without forking CKEditor's Link Plugin (#1643)

Version 0.84.0 (Released January 04, 2023)
--------------

- skip syncing offline build if no offline config exists (#1637)
- add offline build to single course pipeline (#1630)

Version 0.83.1 (Released December 22, 2022)
--------------

- abort onReady if no editor (#1629)
- Cc/disallow simul subsup (#1627)
- Subscripts and superscripts (#1588) (#1617)

Version 0.83.0 (Released December 21, 2022)
--------------

- purge cache on build failures; add alerts (#1623)
- update ckeditor to v35 (#1618)
- themes branch argument for theme assets build (#1616)

Version 0.82.4 (Released December 20, 2022)
--------------

- clean publish for individual sites (#1611)
- Revert "update content dispositions (#1380)" (#1615)
- Fixing typo in GDrive creation management command (#1610)
- Modify RelationField to filter out unpublished content if the website property is present (#1604)
- update content dispositions (#1380)

Version 0.82.3 (Released December 06, 2022)
--------------

- Fix Routing in OCW Studio (#1600)

Version 0.82.2 (Released December 02, 2022)
--------------

- Revert "Subscripts and superscripts (#1588)" (#1597)
- Subscripts and superscripts (#1588)

Version 0.82.1 (Released December 01, 2022)
--------------

- mb/ubuntu_version_2 (#1594)
- hardcode github action to ubuntu-20.04, see if it passes ci tests (#1591)
- Adding management command to delete objects with missing type (#1587)

Version 0.82.0 (Released November 29, 2022)
--------------

- change slack-webhook to slack-url var (#1585)
- Issue slack alert when theme assets pipeline fails (#1576)
- use slug and not name (#1582)

Version 0.81.3 (Released November 29, 2022)
--------------

- filter out mp4 files in the offline mass-build-sites (#1579)

Version 0.81.2 (Released November 17, 2022)
--------------

- Update docker-compose to work with Apple Silicon (#1572)

Version 0.81.1 (Released November 16, 2022)
--------------

- Raising an error when 3Play transcript submission fails (#1569)

Version 0.81.0 (Released November 16, 2022)
--------------

- add site_short_id to JSON file serializer (#1566)

Version 0.80.0 (Released November 09, 2022)
--------------

- sentry-dsn added in theme assets pipeline (#1563)

Version 0.79.1 (Released November 07, 2022)
--------------

- use OCW_COURSE_STARTER_SLUG in pipelines (#1560)

Version 0.79.0 (Released November 02, 2022)
--------------

- Management Command for Renaming Files on S3 (#1538)
- Bump nokogiri from 1.13.6 to 1.13.9 in /docs (#1537)
- ocw hugo themes sentry dsn added  (#1548)
- Use registry-image in concourse pipelines (#1553)
- name offline site zip with short_id instead of name (#1546)

Version 0.78.3 (Released November 01, 2022)
--------------

- give db service a static ip on the concourse network, and appropriately rename it from minio-network to concourse-network (#1540)
- Update eslint-config-mitodl (#1536)

Version 0.78.2 (Released October 26, 2022)
--------------

- update yarn install (#1541)
- Bump moment from 2.29.1 to 2.29.4 (#1531)
- Bump terser from 5.12.1 to 5.15.1 (#1530)
- Bump protobuf from 3.17.3 to 3.18.3 (#1508)
- Bump oauthlib from 3.1.1 to 3.2.1 (#1485)

Version 0.78.1 (Released October 19, 2022)
--------------

- Adding management command to unpublish list of course sites (#1529)
- Pt/read title from pdf metadata (#1516)

Version 0.78.0 (Released October 18, 2022)
--------------

- upgrade version of ocw-course-publisher (#1526)

Version 0.77.1 (Released October 13, 2022)
--------------

- Add ckeditor5 math plugin (#1522)

Version 0.77.0 (Released October 11, 2022)
--------------

- Replace `@ts-ignore` with `@ts-expect-error`, and remove most of them (#1520)

Version 0.76.0 (Released October 06, 2022)
--------------

- increase timeout on copy-s3-buckets (#1515)

Version 0.75.2 (Released October 06, 2022)
--------------

- proper pathing for the zip command (#1507)
- use a different method to check if html files exist (#1505)

Version 0.75.1 (Released September 28, 2022)
--------------

- Adding on_error and on_abort notifications to slack. (#1503)
- Provide a more helpful error log message when something goes wrong w/git authentication (#1494)

Version 0.75.0 (Released September 22, 2022)
--------------

- increase timeout on mass-build-sites (#1500)
- Bring back synced_checksum reset for nonpublished sites after a url change (#1496)
- log ckeditor errors and use sentry/react (#1488)
- Adding functionality to search resources by filename (#1487)
- emulate separate turndown instances (#1490)
- Fix WebsiteContent.full_metadata property (#1489)
- ZIP up offline sites in mass-build-sites (#1477)

Version 0.74.0 (Released September 20, 2022)
--------------

- feat: site dependencies shown while course unpublishing (#1468)
- Remove oauth2client (#1466)
- removed underline PR (#1475)

Version 0.73.0 (Released September 08, 2022)
--------------

- In the mass site build, if building for offline, move any HTML files from content to static (#1471)
- mass build starter filter (#1467)

Version 0.72.2 (Released September 07, 2022)
--------------

- Refactor Youtube token generation (#1459)

Version 0.72.1 (Released September 01, 2022)
--------------

- mass-build-sites offline flag (#1453)

Version 0.72.0 (Released August 31, 2022)
--------------

- Pt/draft content warnings (#1456)

Version 0.71.3 (Released August 31, 2022)
--------------

- Bump lxml from 4.6.5 to 4.9.1 (#1416)
- Bump tzinfo from 1.2.7 to 1.2.10 in /docs (#1423)

Version 0.71.2 (Released August 22, 2022)
--------------

- Pt/resource picker tabs (#1448)

Version 0.71.1 (Released August 15, 2022)
--------------

- don't retry the mass build automatically (#1445)
- clean up mass build sites logging (#1442)

Version 0.71.0 (Released August 11, 2022)
--------------

- Setting default language for code blocks to plain text (#1437)

Version 0.70.1 (Released August 10, 2022)
--------------

- GITKEYSSH not GITSSHKEY (#1432)
- alternate theme rendering - mass build pipeline (#1429)

Version 0.70.0 (Released July 28, 2022)
--------------

- add local s3 storage emulation with minio (#1421)

Version 0.69.0 (Released July 27, 2022)
--------------

- Clean up noisy detect-secrets errors (#1425)

Version 0.68.0 (Released July 18, 2022)
--------------

- Set notifySubscribers to False by default for YouTube videos uploaded through Studio (#1418)

Version 0.67.0 (Released July 14, 2022)
--------------

- added resource list to resource picker (#1412)
- Removing UUID v1 from displayed filenames in Edit Resource drawer (#1415)
- added check to filter undefined tabs (#1411)

Version 0.66.0 (Released July 11, 2022)
--------------

- Added a check for site status (#1405)
- Add Filename to Edit Resource Menu When GDrive Sync Enabled (#1406)

Version 0.65.0 (Released June 30, 2022)
--------------

- fixed small error (#1408)
- add management command set_content_metadata_to_default (#1402)

Version 0.64.0 (Released June 21, 2022)
--------------

- Added permission hook for conditional rendering  (#1389)
- Use common mgmt command options for filtering by websites (#1394)

Version 0.63.4 (Released June 10, 2022)
--------------

- Remove log statement (#1400)
- Option to delete existing pipelines in management commands (#1392)
- update generate_item_metadata to optionally use config default value (#1363)
- Show publishing api errors in publishing drawer (#1367)
- remove two unused dependencies (#1360)
- do not emit declaration files (#1293)

Version 0.63.3 (Released June 09, 2022)
--------------

- Updating nginx version in docker-compose to 1.22.0 (#1397)

Version 0.63.2 (Released June 07, 2022)
--------------

- Always set publish fields in publish_website function (#1383)
- Management command & github api tweak to ensure checksums are current (#1390)

Version 0.63.1 (Released June 02, 2022)
--------------

- Adding information to the body of each slack alert to indicate which pipeline + course failed (#1385)

Version 0.63.0 (Released May 31, 2022)
--------------

- add migration to move metadata description on resources to the markdown body (#1382)

Version 0.62.1 (Released May 31, 2022)
--------------

- Bump pyjwt from 2.1.0 to 2.4.0 (#1374)
- Bump nokogiri from 1.12.5 to 1.13.6 in /docs (#1334)
- Show proper urls on the Publish Drawer (#1377)
- Fix conflicting migrations (#1378)
- feat: Limit site starter options when creating new site (#1355)
- allow setting link / embed on minimal markdown editor (#1364)

Version 0.62.0 (Released May 25, 2022)
--------------

- Custom URL tweaks (#1371)
- added command to update departments (#1256)
- Added slack notifications on_failure cases to the individual site pipelines. (#1358)
- Customizable URLs for studio (#1316)
- improve legacy shortcode handling (#1349)

Version 0.61.1 (Released May 17, 2022)
--------------

- treat shortcodes in resource link text as literal text (#1359)
- make markdown editor minimal by default (#1351)
- short ID added with title in sites list (#1346)
- check for 3play completion (#1345)
- improve frontend shortcode regex to not be fooled by delimiters in shortcode args (#1347)

Version 0.61.0 (Released May 17, 2022)
--------------

- Hid Site Dashboard and refactored component (#1332)
- use anchor not link for external link (#1341)

Version 0.60.3 (Released May 16, 2022)
--------------

- add VIDEO_S3_TRANSCODE_ENDPOINT (#1324)
- Update the prod deploy script to point to prod (#1333)
- Added a github action for production releases. (#1331)
- make retry_on_failure preserve type hints (#1313)

Version 0.60.2 (Released May 12, 2022)
--------------

- Fix deploy configuration
- add API_BEARER_TOKEN to the Hugo step in the site build pipelines (#1329)
- use the proper ocw-course-publisher image and specify version (#1326)

Version 0.60.1 (Released May 11, 2022)
--------------

- update references to the mitodl/ocw-course-publisher docker container to specify version and set it to 0.2 (#1321)
- Fix workflow syntax (#1319)
- updated node version (#1310)
- Added a github action workflow for releasing to CI
- migrate ocw-www content type pages to page (#1312)
- add SITEMAP_DOMAIN to the app and pipeline templates (#1306)

Version 0.60.0 (Released May 11, 2022)
--------------

- make legacy uid hidden (#1304)

Version 0.59.3 (Released May 09, 2022)
--------------

- fix webvtt transcript (#1302)
- redirect to login on authentication failures (#1300)
- Set up one of the transcoded video outputs to be downloadable (#1288)

Version 0.59.2 (Released May 06, 2022)
--------------

- Cc/user store (#1297)

Version 0.59.1 (Released May 04, 2022)
--------------

- Remove stray slash from unpublish pipeline (#1291)

Version 0.59.0 (Released May 03, 2022)
--------------

- Fix mass publish command (#1289)
- Update social auth readme docs (#1284)
- specify yarn version for heroku (#1266)
- rename migration (#1286)
- Unpublish sites - backend code (#1270)
- add migration to move filetype to resourcetype (#1276)
- Fix file paths command (#1261)
- publish alert, prettier prompt, new IntegrationTestHelper
- fix transcript links (#1281)

Version 0.58.0 (Released April 29, 2022)
--------------

- fix erroneous prompting when saving new pages (#1279)
- Added video-gallery to add link ResourceDialogPicker (#1273)
- Added a check to return as soon as filter_set has been gone over (#1257)
- Prompt for confirmation when discarding changes
- New sites API: Filter out sites without sitemetadata content instead of Website.metadata (#1202)

Version 0.57.6 (Released April 25, 2022)
--------------

- added command to migrate testimonials to stories (#1250)
- Sync Website.title with the sitemetadata course_title (#1244)

Version 0.57.5 (Released April 21, 2022)
--------------

- set `YT_FIELD_DESCRIPTION` to `video_metadata.youtube_description` (#1253)
- Escape quotes in resource link text (#1249)

Version 0.57.4 (Released April 20, 2022)
--------------

- [markdown cleanup] <, > to «, » (#1245)
- Rename mass-publish pipeline to mass-build-sites, refactor mass-publish command (#1246)
- [markdown cleanup] fix superscript/subscript escaping issues (#1241)
- fix: course_collections renamed to course-collection (#1239)

Version 0.57.3 (Released April 15, 2022)
--------------

- fix: required=true for relation widgetvariant (#1240)

Version 0.57.2 (Released April 12, 2022)
--------------

- improve link logging (#1235)

Version 0.57.1 (Released April 12, 2022)
--------------

- remove delete_unpublished_courses (#1234)
- Update filter for the mass-publish api endpoint (#1229)
- Sync videos from Google Drive files_final folder, don't transcode or upload to Youtube (#1227)
- Avoid unnecessary dupe transcode jobs, retry on gdrive->s3 upload errors a few times before raising (#1219)
- Preserve querystrings when paginating (#1226)

Version 0.57.0 (Released April 11, 2022)
--------------

- Allow selection of null values for website publish fields in Django admin (#1224)

Version 0.56.4 (Released April 08, 2022)
--------------

- Cc/default active tab (#1216)
- prevent mass import (#1214)
- add "other" tab to resource picker (#1210)

Version 0.56.3 (Released April 07, 2022)
--------------

- Cc/convert link wrapped images (#1206)

Version 0.56.2 (Released April 05, 2022)
--------------

- Sort websites by first_published_to_production (#1204)

Version 0.56.1 (Released April 05, 2022)
--------------

- update fastly vars for mass-publish pipeline definition (#1199)
- Revert API change (#1200)
- Handle courses with no instructors (#1196)
- Get gdrive file body via the google drive api and stream that to s3 (#1169)
- tolerate href, href_uid on resource shortcode (#1192)
- Use first_published_to_production instead of publish_date for sorting new courses, get metadata from WebsiteContent (#1191)

Version 0.56.0 (Released April 04, 2022)
--------------

- Added some metrics for celery task completion time

Version 0.55.2 (Released March 31, 2022)
--------------

- replace ocwnext with ocw (#1185)
- handle links/images inside links correctly (#1178)
- Convert more baseurl links to resource_links  (#1174)

Version 0.55.1 (Released March 30, 2022)
--------------

- Use get_redis_connection("redis").client() instead of app.backend.client (#1181)
- Fix rootrelative URLs to duplicate files

Version 0.55.0 (Released March 28, 2022)
--------------

- Set a configurable limit to the number of redis pool connections (#1170)
- don't update fields that don't exist in resource data (#1166)

Version 0.54.4 (Released March 28, 2022)
--------------

- set parent_id when overwriting metadata.parent_uid (#1115)
- use pyparsing for link paring + resolveuid fix
- remove image inacessible (#1158)

Version 0.54.3 (Released March 24, 2022)
--------------

- changed italic delimiter to "*" (#1147)

Version 0.54.2 (Released March 23, 2022)
--------------

- Fix gdrive import for ocw-www (#1155)
- fix a typo in the localdev config
- only query with published = true if cross_site is also true (#1109)

Version 0.54.1 (Released March 22, 2022)
--------------

- Use pyparsing for some markdown replacements

Version 0.54.0 (Released March 21, 2022)
--------------

- tweak internal site search (#1134)
- Handle authentication for Concourse 7.7 (#1120)
- tolerate quotes around resource, resource_link uuids (#1136)
- add localdev support for course collection, list
- fix a small issue with the website search

Version 0.53.5 (Released March 17, 2022)
--------------

- Allow mass-publish to process a list of site names from a json file or comma-delimited string (#1127)

Version 0.53.4 (Released March 17, 2022)
--------------

- Option to sync a specific commit/path from github to the database (#1108)
- add inline code support to ckeditor

Version 0.53.3 (Released March 16, 2022)
--------------

- default metadata to empty object before iterating in seralizer (#1129)

Version 0.53.2 (Released March 15, 2022)
--------------

- theme assets build cache busting take 3 (#1121)

Version 0.53.1 (Released March 15, 2022)
--------------

- cc/fix-relative-metadata-links

Version 0.53.0 (Released March 14, 2022)
--------------

- Revert "theme assets build cache busting take 2 (#1103)" (#1117)
- theme assets build cache busting take 2 (#1103)

Version 0.52.2 (Released March 09, 2022)
--------------

- Improved site search for names, short_ids (#1092)
- Fix / Convert rootrelative urls (#1086)

Version 0.52.1 (Released March 09, 2022)
--------------

- Revert "purge theme assets after deployment (#1090)" (#1096)
- merge new metadata with old metadata (#1094)
- purge theme assets after deployment (#1090)

Version 0.52.0 (Released March 08, 2022)
--------------

- adjust PR template
- add code block support to CKEditor
- Add option to add new content and modify nested metadata for overwrite_ocw_course_content command (#1071)

Version 0.51.0 (Released March 03, 2022)
--------------

- fix spacing issue w/ single-line text inside of table cells

Version 0.50.0 (Released March 02, 2022)
--------------

- fix line break in table cells issue

Version 0.49.0 (Released March 02, 2022)
--------------

- move website content drawer open / close / edit state to URL
- change resource_link delimiters to % instead of < > (#1067)
- pass the --buildDrafts argument to Hugo if building a preview (#1062)

Version 0.48.0 (Released March 01, 2022)
--------------

- When syncing from git to db, `file` value should only include the path, not domain (#1056)

Version 0.47.9 (Released February 25, 2022)
--------------

- encode data-uuid passed to CKEditor (#1063)
- Add metadata to mediaconvert job for filtering, based on queue name (#1018)
- Cc/collections limited (#1055)
- Add open webhook to pipelines (#1028)
- Update ContentSyncState checksums when bulk updating WebsiteContent (#1047)
- convert baseurl links w/ fragments (#1036)
- Enforce youtube length limits when uploading/updating title, description (#1009)

Version 0.47.8 (Released February 24, 2022)
--------------

- Enable linking to resource and course collections
- add content filtering to the website content listing page

Version 0.47.7 (Released February 23, 2022)
--------------

- support resource link anchor IDs

Version 0.47.6 (Released February 18, 2022)
--------------

- baseurl replacement improvements (#1034)
- Separate celery queues for publish tasks, batch tasks (#1031)
- Handle youtube 403s and update website publish status immediately on errors (#1007)

Version 0.47.5 (Released February 18, 2022)
--------------

- add GTM_ACCOUNT_ID to OCW site builds (#1027)
- add 'published' param to content listing API

Version 0.47.4 (Released February 17, 2022)
--------------

- add markdown cleanup rule for legacy data fix (#1024)
- Make embeddable=True explicit when updating youtube metadata status (#1022)
- convert resource_file to resource shortcodes (#1016)

Version 0.47.3 (Released February 17, 2022)
--------------

- add support for nondestructive editing w/ legacy shortcodes

Version 0.47.2 (Released February 17, 2022)
--------------

- Only update metadata for youtube videos with associated VideoFile objects (#1014)
- add management command markdown_cleanup_baseurl (#1002)
- small tech debt thing
- improvements to the site search

Version 0.47.1 (Released February 15, 2022)
--------------

- type -> ocw_type (#1004)
- improvements to search handling on the Website listing API
- Blank _logo.html to remove default logo image (#997)

Version 0.47.0 (Released February 14, 2022)
--------------

- Prevent endlessly incrementing short-ids on imported sites, new command to fix affected sites (#988)

Version 0.46.0 (Released February 14, 2022)
--------------

- When resetting sync state, the data field should also be set to None (#946)

Version 0.45.0 (Released February 11, 2022)
--------------

- fix: youtube video thumbnail 0.jpg replaced with default.jpg (120x90) (#985)
- set serial: true on the mass publish job (#987)
- remove italicization of text within blockquote tags in CKEditor
- Setting the resources for the individual sites to `check_every: never`. See https://concourse-ci.org/resources.html. This makes sense because the individual pipelines will now only ever be triggered by webhooks (`trigger: false` is set on all of them). (#982)
- add OCW_IMPORT_STARTER_SLUG to the mass publish pipeline definition code (#984)

Version 0.44.1 (Released February 10, 2022)
--------------

- import for learning_resource_types (#980)

Version 0.44.0 (Released February 08, 2022)
--------------

- copy webpack.json into base-theme instead of into the site's data folder (#977)

Version 0.43.1 (Released February 04, 2022)
--------------

- refactor logic for indicating the site content form has been touched
- Fix pipeline webhook (#970)
- Codify new mass publish pipeline and api endpoint (#950)
- scroll to form errors on submission (#962)
- use governmentpaas/s3-resource for the webpack-json resource to be compatible with using versioned_file with IAM authentication (#966)
- Bump ipython from 7.19.0 to 7.31.1 (#920)
- fix up our handling of the camelcase eslint rule a little bit
- add webpack-json as an input to the build-course-task pipeline step (#961)
- [UI] prevent duplicate items in collections (#951)
- theme assets pipeline (#945)
- remove a @ts-ignore
- small rename of two functions for clarity

Version 0.43.0 (Released January 31, 2022)
--------------

- add yarn.lock
- only make clickable list items have cursor pointer
- remove unused css class card-content
- use margins to separate list items, not padding
- fix issue with website name not being saved in resource collection
- reconcile ckedidtor, showdown multiline list items
- add an optional filter to the website listing API for publish status

Version 0.42.3 (Released January 28, 2022)
--------------

- move pipeline api callbacks to jgriff/http-resource (#937)
- update postgres to 12.8 to match prod

Version 0.42.2 (Released January 27, 2022)
--------------

- Add option of github authentication via app (#914)

Version 0.42.1 (Released January 26, 2022)
--------------

- Upgrade celery (#919)
- move comment above declaration
- move regex back up
- support merging of table cells (#899)
- fix resource_link regex, make non-greedy
- update handling of publish_date field on the Website model

Version 0.42.0 (Released January 25, 2022)
--------------

- ocw_import_course_sites - sync to github by default (#921)
- some test cleanup
- enable linking to pages within a course

Version 0.41.1 (Released January 21, 2022)
--------------

- Limit git api rate for all current batch functions that use it at high volume (#909)

Version 0.41.0 (Released January 20, 2022)
--------------

- remove 'legacy' implementation of WebsiteCollections

Version 0.40.1 (Released January 18, 2022)
--------------

- add -p to mkdir command before theme asset extraction (#900)

Version 0.40.0 (Released January 13, 2022)
--------------

- "waterfall" triggering scheme for ocw-hugo-themes changes (#891)
- switch from storing website UUID to the website name property
- add support for 'website-collection' field

Version 0.39.1 (Released December 23, 2021)
--------------

- Revert "use static version file as trigger for sites other than ocw-www (#881)" (#883)
- use static version file as trigger for sites other than ocw-www (#881)

Version 0.39.0 (Released December 21, 2021)
--------------

- Retry all pipeline steps up to 3x (#864)
- Descriptive message on front end for publishing warnings (#867)
- add uids to metadata output
- Fix a bad query (#877)

Version 0.38.0 (Released December 20, 2021)
--------------

- Fix task bug caused by decorator (#873)
- Fix Youtube API status update call (#875)
- Bump lxml from 4.6.3 to 4.6.5 (#868)
- Split sortable UI off from RelationWidget into SortableSelect component
- Run incomplete_publish_build_statuses task only if a pipeline backend is set (#851)
- set up swc for jest, webpack
- Bump django from 3.1.13 to 3.1.14 (#866)
- Log an error when a pipeline fails (#854)
- Make youtube videos public for live publishing (#850)
- remove an unused dependency
- Fix outdated starter configs, add README instructions to update them via mgmt command (#858)
- Avoid certain WebsiteContent filenames (#855)
- Concourse in a docker container (#852)
- add site search

Version 0.37.5 (Released December 14, 2021)
--------------

- Add all metadata keys w/blank values for imported google drive content (#860)

Version 0.37.4 (Released December 09, 2021)
--------------

- refactor fix for deleting orphaned git files (#849)
- import video galleries (#848)
- Do not show menu dropdown for global admins or site owner (#844)
- Remove old pages and content (#843)

Version 0.37.3 (Released December 03, 2021)
--------------

- use task decorator to prevent multiple instances of recurring scheduled tasks from running at once (#832)
- Populate additional fields when publishing via mass_publish (#840)
- move from casual-browserify to the normal package

Version 0.37.2 (Released December 02, 2021)
--------------

- update typescript a little bit
- upgrade ckeditor packages to the latest version
- Use concourse webhooks plus periodic task to update publish status (#820)
- make title the default text inside of a resource link
- Ignore anything in parentheses for short_id (#830)
- remove Dockerfile-node
- remove an unnecessary step from our CI setup
- fix callback url
- conditionally set the modal titlee on menu page for editing, adding
- Remove some unnecessary mocks of `global.fetch`

Version 0.37.1 (Released November 30, 2021)
--------------

- add cross_site option to the Relation field
- Fix publish bug (#821)
- Add option to delete git files not matching WebsiteContent in db (#812)
- Handle all cases of youtube_id being null (#816)
- Mass publish sites management command (trigger_pipelines -> mass_publish) (#801)
- Fix changing short_id on ocw reimport, reset publish fields as part of `reset_sync_state` command (#809)
- Show confirmation dialog when data would be lost (#799)
- Always unpause pipelines before triggering (#811)

Version 0.37.0 (Released November 19, 2021)
--------------

- transcript notifications

Version 0.36.0 (Released November 15, 2021)
--------------

- Create gdrive folders for imported sites if unassigned (#798)
- Fix some issues with upserting multiple site pipelines (#794)

Version 0.35.1 (Released November 12, 2021)
--------------

- automate transcript upload
- Trigger concourse build via API (#783)

Version 0.35.0 (Released November 09, 2021)
--------------

- fix an issue with the migration to deal with bad data (#787)
- Poll for gdrive folder if blank on resources page (#781)
- Update various pages to use new, Card-based designs
- make sure menu items never have zero weight (#775)
- Tweak WebsiteContent permissions (#772)
- Send publish email within polling task and only to the publish requester (#766)
- upgrade to yarn 3
- Fix several celery task bugs (#774)
- add a 404 page for a missing site
- add page titles

Version 0.34.0 (Released November 08, 2021)
--------------

- Sync status frontend (#758)
- Handle level import, add term and year to metadata (#757)

Version 0.33.0 (Released November 02, 2021)
--------------

- add error handling to the Relation field request
- Fix poll_build_status_until_complete to use celery countdown instead of sleep (#763)

Version 0.32.2 (Released November 02, 2021)
--------------

- add ocw-www site dependency to readme
- fix image alignment issue
- Filter resourcetype on backend for website content (#742)
- add support for editing table shortcodes to the markdown editor
- Track sync status backend, w/fixed migration (#751)

Version 0.32.1 (Released November 01, 2021)
--------------

- Change ContentDisposition for videos
- Revert "Track website sync status - backend (#734)" (#750)
- Track website sync status - backend (#734)
- Upgrade sentry (#697)
- Fix flaky test (#739)
- Privacy policy page and home page tweaks (#737)
- Implement publish status UI (#705)
- switching over a bunch of test files to use the new mockRequest functions

Version 0.32.0 (Released October 28, 2021)
--------------

- Open publish site links in new tab (#729)
- Show google drive links (#720)
- Use name instead of short_id for resource S3 keys (#726)
- add to validation schema, add an example thing in there

Version 0.31.0 (Released October 22, 2021)
--------------

- Make check for rate limits optional in sync_unsynced_websites task (#721)
- Slugify s3 keys and make sure they're still unique (#710)
- Hide production publish btn, prohibit metadata editing for non-admin editors (#702)
- Hide the file upload field on resource form if google drive integration is enabled (#712)
- add a line to .gitignore
- update ocw_import (#715)
- Fix flaky test (test_format_recipient) (#713)
- small fix for UX issue on website collections page
- Fix bug in create_gdrive_folders (#704)

Version 0.30.4 (Released October 18, 2021)
--------------

- remove title from hugo menu serialization (#703)
- remove some unneeded testing code

Version 0.30.3 (Released October 14, 2021)
--------------

- Updated common UI elements and basic page layout to match new designs
- disallow nested tables

Version 0.30.2 (Released October 13, 2021)
--------------

- fix issue preventing opening MenuField dialog

Version 0.30.1 (Released October 13, 2021)
--------------

- use theme assets from RC for now (#686)
- Update website publish date for singleton content (#684)
- Copy gdrive mime_type to file_type in content  metadata (#683)
- Added redesigned site header

Version 0.30.0 (Released October 12, 2021)
--------------

- Ignore drive folders with no download links, handle null checksums (#666)
- Fix google drive sync bug with pages (#676)
- Do a hard or soft fastly purge based on settings (#671)
- Autocreate all gdrive resources, fix github syncing for them (#630)
- Leave new pipelines paused until previewed/published for the first time (#662)

Version 0.29.2 (Released October 12, 2021)
--------------

- add tables to CKEditor config for Markdown editor #645
- Ensure that delete_unpublished_courses runs only after all courses have finished importing (#649)
- Dont instantiate the YouTubeAPI class unless it has something to do (#661)
- update url-assembler typedef so we can remove @ts-ignore
- change how URL matching works in IntegrationTestHelper
- Set site-id metadata during pipeline s3 sync (#660)
- Use text_id from frontend when creating WebsiteContent (#656)
- prefix destination urls with / to make them root relative (#657)

Version 0.29.1 (Released October 07, 2021)
--------------

- Site publish drawer (#623)
- Management command for resetting synced checksums and optionally syncing all github repos (#644)
- when serializing Hugo markdown files, write out the WebsiteContent type property as content_type and deserialize that back into type (#646)
- Save file location to WebsiteContent.file for imported OCW courses (#635)
- style / layout / ux updates to the resource picker
- Bump nokogiri from 1.11.4 to 1.12.5 in /docs (#610)
- Bump django from 3.1.12 to 3.1.13 (#595)

Version 0.29.0 (Released October 04, 2021)
--------------

- Tweak s3 path for gdrive-imported nonvideo files (#611)
- Additional env variables for concourse pipelines (#632)

Version 0.28.0 (Released October 01, 2021)
--------------

- Fix bug so slug field is used for filename (#625)
- Trim content from destination url (#627)
- import additional metadata (#622)
- remove unnecessary changes to the webpack config
- allow users to create inline links to resources
- remove media embed plugin button from Markdown editor toolbar
- Rename duplicate names during ocw-import (#603)
- Front-end for google drive syncing (#604)
- dependency upgrade
- Sync all files in Google Drive (#591)
- Add slug field to set a different value for filenames of content (#600)

Version 0.27.0 (Released September 28, 2021)
--------------

- Remove if check on dirpath == content/page (#602)
- add license
- use course_legacy.json instead of course.json, update topics import, update test data, mock out parent / child test (#599)
- Add pragma: allowlist secret to ignore false positives for secret detection (#597)
- Populate file_type on file upload (#573)

Version 0.26.1 (Released September 27, 2021)
--------------

- Omit file url from payload (#587)
- upload youtube transcript
- course_feature_tags-> learning_resource_types

Version 0.26.0 (Released September 21, 2021)
--------------

- Only run `update_youtube_thumbnail` when appropriate (#586)
- Handle bool as string returned by concourse pipeline request (#582)
- update transcript metadata

Version 0.25.1 (Released September 17, 2021)
--------------

- fix video preview on resource embed
- Bump addressable from 2.7.0 to 2.8.0 in /docs (#379)
- Youtube metadata update (#562)
- Failure message for bad concourse builds (#566)

Version 0.25.0 (Released September 15, 2021)
--------------

- transcript sync

Version 0.24.0 (Released September 09, 2021)
--------------

- Add support for linking to resources in the Markdown editor
- Youtube upload email notifications (#535)
- run some dependency upgrades
- add rich display for videos embedded in markdown editor

Version 0.23.4 (Released September 07, 2021)
--------------

- delete unpublished courses take two (#551)
- Fix course site config (#549)
- update import code and test data to reflect latest ocw-to-hugo changes (#532)
- Upload videos to YouTube (#484)
- Revert "delete unpublished courses originally imported from ocw-to-hugo (#526)" (#543)
- add display of embedded images in Markdown editor
- Update local ocw course site config to match ocw-hugo-projects (#538)

Version 0.23.3 (Released September 01, 2021)
--------------

- Only show "Add resource" button when attach field is set (#530)
- Add identifier for external links to import_ocw_course_sites (#527)

Version 0.23.2 (Released September 01, 2021)
--------------

- Upgrade the ckeditor packages and webpack
- delete unpublished courses originally imported from ocw-to-hugo (#526)
- Make starter required for OCW_IMPORT_STARTER_SLUG (#516)
- Add resource picker to Markdown editor

Version 0.23.1 (Released August 30, 2021)
--------------

- when importing ocw-to-hugo courses and creating instructors, mark those instructors is_page_content = True, set the correct dirpath and set the filename to the text_id (#518)

Version 0.23.0 (Released August 26, 2021)
--------------

- Transcode videos with AWS MediaConvert (#469)
- gdrive folder creation
- remove course_id prefix on dirpath of imported course content (#513)
- Hide hidden fields inside object fields (#498)
- add the get_destination_url helper function and use it for menu urls (#496)
- make UUID check version agnostic by default and add tests (#509)
- add in-editor display of embedded resources
- Fix attach: "resource" (#501)
- Topics UI and backend (#471)
- Add rule to require one of files or folder in collection schema (#492)
- Bump yamale from 3.0.4 to 3.0.8 (#485)
- Use yaml.SafeLoader (#489)

Version 0.22.1 (Released August 24, 2021)
--------------

- Add custom format_recipient function, assign to MITOL_MAIL_FORMAT_RECIPIENT_FUNC (#483)
- add resource embed UI
- upgrade eslint config, remove some unneeded packages

Version 0.22.0 (Released August 12, 2021)
--------------

- add OCW_IMPORT_STARTER_SLUG setting and update included testing config (#468)
- Draft/live publish notifications (#381)
- some JS dependency upgrades
- Google Drive integration (#431)
- check for identifier before accessing it (#473)

Version 0.21.2 (Released August 05, 2021)
--------------

- fix drawer width bug

Version 0.21.1 (Released August 04, 2021)
--------------

- switch site content modal over to ModalState
- Fix for multiple field types in content_context (#449)

Version 0.21.0 (Released August 04, 2021)
--------------

- import menus.yaml files as navmenus and update test data (#448)
- Adjust get_short_id function (#444)
- add resource widget plugin for CKEditor
- Reduce default chunk size for import_ocw_course_sites (#446)
- Remove text_id parameter, instead use content_context for MenuField (#428)
- add UI for deleting websites from a WebsiteCollection
- Use both website name and content textId for lookup (#435)
- Handle valuesToOmit when value is a list (#433)
- Write task id to console for import_ocw_course_sites (#439)

Version 0.20.2 (Released August 03, 2021)
--------------

- Use debounced fetch for website collection course search (#432)
- add an 'act' to get rid of some warnings
- Fix null website error with RelationField (#414)
- Fixed Hugo nav menu format
- Create and sync sitemetadata with instructors (#409)
- Add preventDefault to menu buttons (#427)
- Use async search for RelationField widget (#402)

Version 0.20.1 (Released July 29, 2021)
--------------

- Replace "course_numbers" with "primary_course_number", "extra_course_numbers" in sample json and in get_short_id function (#423)
- Async search backend (#407)
- Add uniqBy to remove duplicate options for website collection UI (#422)
- Add index to WebsiteContent.title and Website.title (#421)
- fix comment typo
- Website.short_id for repo names (#405)

Version 0.20.0 (Released July 27, 2021)
--------------

- Fix version/bucket mismatch in pipeline configuration (#417)
- Pipeline management commands (#388)
- Concourse pipelines, take 2 (#399)
- add WebsiteCollectionItem editing UI
- Create README.md (#380)

Version 0.19.1 (Released July 26, 2021)
--------------

- Revert "Generate concourse pipelines on website creation (#366)" (#389)
- Publish button (#374)
- add WebsiteCollection editing functionality
- Upgrade mitol-django-authentication, common, pygithub (#373)
- Generate concourse pipelines on website creation (#366)

Version 0.19.0 (Released July 13, 2021)
--------------

- Added back-end for configuring navigation menus
- add WebsiteCollection list / index page
- Added front-end for configuring navigation menus
- Add label_singular field for collections (#353)
- add documentation comment for two types

Version 0.18.0 (Released July 07, 2021)
--------------

- remove a few unneeded ts-ignore comments
- Fix handling of empty values in new content (#360)
- add APIs for WebsiteCollections and WebsiteCollectionItems

Version 0.17.4 (Released July 01, 2021)
--------------

- Get site/file url prefix from site config (#338)
- Skip validation if fields are not visible (#351)

Version 0.17.3 (Released July 01, 2021)
--------------

- Fix pylint (#348)
- Remove GIT_TOKEN precondition check in content_sync.api.sync_github_website_starters (#347)
- Github webhook branch filter (#343)

Version 0.17.2 (Released June 29, 2021)
--------------

- Implement linking to content in other websites
- Fix object field validation (#342)
- added serializers for the website collection related objects

Version 0.17.1 (Released June 25, 2021)
--------------

- Include uploaded filepath in backend (github) metadata (#333)
- Filter out course sites with null metadata (#327)
- Allow WebsiteContent file upload fields to have any name, not just "file" (#329)
- Add MarkdownEditor tests (#330)
- Bump postcss from 7.0.35 to 7.0.36 (#326)
- Bump django from 3.1.8 to 3.1.12 (#318)
- Added omnibus site config and pared down course config
- Made 'title' field default for 'folder'-type items

Version 0.17.0 (Released June 23, 2021)
--------------

- add models, admin config, and the migration for the WebsiteCollection

Version 0.16.3 (Released June 09, 2021)
--------------

- Do not use git token in sync_starter_configs function (read-only from public repo) (#313)
- don't fail build if coverage upload doesn't work
- API endpoint for creating/updating starters from github webhooks (#297)
- Restrict routes not used to login or view home page (#299)

Version 0.16.2 (Released June 09, 2021)
--------------

- upgrade jest and a few other things
- Bump nokogiri from 1.11.1 to 1.11.4 in /docs (#277)
- Update publish_date when published (#290)
- Added management commands for syncing sites to and from backend

Version 0.16.1 (Released June 02, 2021)
--------------

- Add support for filtering in the relation widget

Version 0.16.0 (Released June 02, 2021)
--------------

- Remove (transaction=true) from @pytest.mark.django_db in a test (#285)
- Bump django from 3.1.6 to 3.1.8 (#204)
- Merge main branch to release branch for publish (#282)
- Revert "import metadata and config (#283)" (#286)
- import metadata and config (#283)
- split out types for ConfigField
- add relation field widget
- small package version bump
- upgrade our eslint configuration to the latest version
- Removed WebsiteContent.content_filepath field

Version 0.15.2 (Released June 01, 2021)
--------------

- Finalized logic for determining target file path for WebsiteContent objects

Version 0.15.1 (Released May 14, 2021)
--------------

- Added WebsiteContent filename and dirpath fields
- Website preview button (#256)
- Github integration section in the README (#248)
- Fixed is_page_content flag bug

Version 0.15.0 (Released May 12, 2021)
--------------

- remove tag for review
- Preview and publish api functions, tasks, endpoints (#253)
- Fixed content/file serialization and deserialization
- remove 'rules of hooks' violation
- Try to fix ubuntu (#257)
- Added support for soft/hard deletes of content

Version 0.14.2 (Released May 06, 2021)
--------------

- Handle filepath changes when syncing with github (#242)

Version 0.14.1 (Released May 05, 2021)
--------------

- node-sass -> sass

Version 0.14.0 (Released May 04, 2021)
--------------

- Customize github api url (#239)

Version 0.13.1 (Released April 30, 2021)
--------------

- Moved collaborator view tests
- add support for the 'Object' field type
- Hide the login button if the user is logged in
- Differentiate between types of user-entered data

Version 0.13.0 (Released April 28, 2021)
--------------

- Github backend and API wrapper (#216)

Version 0.12.0 (Released April 26, 2021)
--------------

- Added optional 'limit' param to OCW course site import

Version 0.11.2 (Released April 26, 2021)
--------------

- Implemented correct UI for 'files' config items
- Add validation for multiple select, min / max

Version 0.11.1 (Released April 22, 2021)
--------------

- make links in the editor more obvious

Version 0.11.0 (Released April 21, 2021)
--------------

- Implement BaseSyncBackend

Version 0.10.1 (Released April 20, 2021)
--------------

- Added data model for ContentSyncState
- Merge add and edit content forms

Version 0.10.0 (Released April 14, 2021)
--------------

- Cleaning up collaborator api
- Create content_sync app
- Use SelectField widget for all select fields site-wide (#201)
- upgrade CKEditor packages to 27.0.0
- remove edit button from 'folder' type
- Added management command to ensure single source of truth for example config files

Version 0.9.1 (Released April 12, 2021)
-------------

- Changed config to user 'folder'/'files' collections types
- Implement hidden widget (#164)
- Implement conditional fields (#161)

Version 0.9.0 (Released April 08, 2021)
-------------

- Map fullname to name in social auth
- use textarea for 'Text' type fields, rather than a normal input tag
- rename javascript-tests to frontend-tests
- use WidgetVariant constants more widely
- fix a few font-size issues
- Collaborator add/edit modal drawer (#173)
- Add settings for using X-Forwarded-* headers
- Content -> Body (#174)
- Integrate Touchstone login
- Fix file upload (#169)
- implement boolean site content widget

Version 0.8.1 (Released April 06, 2021)
-------------

- Implement select widget (#151)
- Bump pygments from 2.6.1 to 2.7.4 (#162)
- fix a padding issue in the site sidebar

Version 0.8.0 (Released March 30, 2021)
-------------

- Added common widget options (required flag and help text)
- Bump pyyaml from 5.3.1 to 5.4 (#156)
- fix issue with list styling on site pages
- update site sidebar to match design

Version 0.7.1 (Released March 24, 2021)
-------------

- fix double-instantiation issue w/ ckeditor
- Skip noncourse files, log error on missing uuid (#127)
- Added first version of site config schema + validation
- Bump django from 3.1 to 3.1.6
- Added minimal markdown as site content widget option
- Moved site content widget components to 'widgets' folder
- first round of styling updates
- Update README with clearer local dev starter/config instructuons
- Updated app to use new site config structure

Version 0.7.0 (Released March 19, 2021)
-------------

- Increase z-index for ckeditor balloons (#123)
- add url-assembler
- Add pagination to content UI (#116)
- Remove comment tags (#118)
- Fix markdown error (#117)
- File Upload UI (#105)
- Add site listing at site dashboard (#108)
- add a minimal configuration of CKEditor
- update ckeditor docs to cover extending markdown syntax
- fix turndown bug relating to <li> tags
- update ocw import to match new ocw-to-hugo output structure (#104)

Version 0.6.2 (Released March 15, 2021)
-------------

- add CKEditor media embed plugin
- File uploads API for WebsiteContent  (#100)
- Page content UI (#94)

Version 0.6.1 (Released March 09, 2021)
-------------

- Collaboration UI (#83)
- add documentation for CKEditor plugin architecture
- Bump cryptography from 3.2 to 3.3.2

Version 0.6.0 (Released March 02, 2021)
-------------

- add markdown support to ckeditor
- Use 'string' for description instead of 'markdown' (#97)
- Add metadata to list of editable fields (#95)
- Turn off pagination for website content API (#91)
- Added site creation page

Version 0.5.2 (Released February 26, 2021)
-------------

- Add underlining to CKEditor
- Add API for WebsiteContent (#84)
- Use resource for content type instead of file (#85)
- Add basic CKEditor setup and test page

Version 0.5.1 (Released February 23, 2021)
-------------

- Website collaboration API (#72)

Version 0.5.0 (Released February 22, 2021)
-------------

- Site detail page (#71)
- Fix import for backpopulate_groups (#79)
- Add select_related to fix n+1 query (#77)

Version 0.4.2 (Released February 19, 2021)
-------------

- Remove settings regarding reloading worker processes (#76)
- Lookup websites by name instead of uuid (#73)

Version 0.4.1 (Released February 18, 2021)
-------------

- Fix typo in webpack-related environment variable (#67)

Version 0.4.0 (Released February 18, 2021)
-------------

- Fix API (#69)
- Integrate permissions with WebsiteViewSet (#65)
- Add common
- Set correct starter on imported sites and moved more OCW code
- Website CRUD permissions (#49)
- a few little frontend tweaks
- Changed WebsiteStarter.config to store JSON instead of YAML
- Detail view for websites (#54)

Version 0.3.0 (Released February 11, 2021)
-------------

- Decoupled 'websites' app from OCW course site import logic
- few more frontend tweaks
- Added website starter API endpoints and feature flag
- a few JS dependency upgrades
- update frontend setup
- Added WebsiteStarter model with local development support

Version 0.2.0 (Released January 26, 2021)
-------------

- Fix black formatting check (#31)
- Added params to backpopulate_ocw_courses command
- Set default pull request template (#29)
- log errors and continue loop instead of exiting, handle some ocw-to-hugo issues like invalid dates that should be null (#26)

Version 0.1.0 (Released January 19, 2021)
-------------

- API view for new courses (#19)

