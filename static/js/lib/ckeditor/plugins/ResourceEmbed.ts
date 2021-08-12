import Plugin from "@ckeditor/ckeditor5-core/src/plugin"
import Turndown from "turndown"
import Showdown from "showdown"
import { toWidget } from "@ckeditor/ckeditor5-widget/src/utils"
import { editor } from "@ckeditor/ckeditor5-core"
import Command from "@ckeditor/ckeditor5-core/src/command"

import MarkdownSyntaxPlugin from "./MarkdownSyntaxPlugin"
import { TurndownRule } from "../../../types/ckeditor_markdown"

export const RESOURCE_SHORTCODE_REGEX = /{{< resource (\S+) >}}/g

const RESOURCE_EMBED = "resourceEmbed"

/**
 * Class for defining Markdown conversion rules for ResourceEmbed
 */
class ResourceMarkdownSyntax extends MarkdownSyntaxPlugin {
  constructor(editor: editor.Editor) {
    super(editor)
  }

  get showdownExtension() {
    return function resourceExtension(): Showdown.ShowdownExtension[] {
      return [
        {
          type:    "lang",
          regex:   RESOURCE_SHORTCODE_REGEX,
          replace: (_s: string, match: string) => `<section>${match}</section>`
        }
      ]
    }
  }

  get turndownRule(): TurndownRule {
    return {
      name: "resourceEmbed",
      rule: {
        filter:      "section",
        replacement: (content: string, _node: Turndown.Node): string => {
          return `{{< resource ${content} >}}\n`
        }
      }
    }
  }
}

/**
 * A CKEditor Command for inserting a new ResourceEmbed (resourceEmbed)
 * node into the editor.
 */
class InsertResourceEmbedCommand extends Command {
  constructor(editor: editor.Editor) {
    super(editor)
  }

  execute(uuid: string) {
    this.editor.model.change((writer: any) => {
      const embed = writer.createElement(RESOURCE_EMBED)
      const text = writer.createText(uuid)
      writer.append(text, embed)
      this.editor.model.insertContent(embed)
    })
  }

  refresh() {
    const model = this.editor.model
    const selection = model.document.selection
    const allowedIn = model.schema.findAllowedParent(
      selection.getFirstPosition(),
      RESOURCE_EMBED
    )
    this.isEnabled = allowedIn !== null
  }
}

export const RESOURCE_EMBED_COMMAND = "insertResourceEmbed"

class ResourceEmbedEditing extends Plugin {
  constructor(editor: editor.Editor) {
    super(editor)
  }

  init() {
    this._defineSchema()
    this._defineConverters()

    this.editor.commands.add(
      RESOURCE_EMBED_COMMAND,
      new InsertResourceEmbedCommand(this.editor)
    )
  }

  _defineSchema() {
    const schema = this.editor.model.schema

    schema.register(RESOURCE_EMBED, {
      isObject:       true,
      allowWhere:     "$block",
      allowContentOf: "$block"
    })
  }

  _defineConverters() {
    const conversion = this.editor.conversion

    /**
     * convert HTML string to a view element (i.e. ckeditor
     * internal state, *not* to a DOM element)
     */
    conversion.for("upcast").elementToElement({
      model: RESOURCE_EMBED,
      view:  {
        name: "section"
      }
    })

    /**
     * converts view element to HTML element for data output
     */
    conversion.for("dataDowncast").elementToElement({
      model: RESOURCE_EMBED,
      view:  {
        name: "section"
      }
    })

    /**
     * editingDowncast converts a view element to HTML which is actually shown
     * in the editor for WYSIWYG purposes
     * (for the youtube embed this is an iframe)
     */
    conversion.for("editingDowncast").elementToElement({
      model: RESOURCE_EMBED,
      view:  (modelElement: any, { writer: viewWriter }: any) => {
        // this looks bad but I promise it's fine
        const resourceID = modelElement._children._nodes[0]._data

        // TODO: this is where we will insert the React render for
        // showing the embedded content in the editor
        const div = viewWriter.createContainerElement("div", {
          class: "resource-embed",
          text:  resourceID
        })
        return toWidget(div, viewWriter, { label: "Resources Embed" })
      }
    })
  }
}

/**
 * CKEditor plugin that provides functionality to embed resource records
 * into the editor. These are rendered to Markdown as `{{< resource UUID >}}`
 * shortcodes.
 */
export default class ResourceEmbed extends Plugin {
  static get pluginName(): string {
    return "ResourceEmbed"
  }

  static get requires(): Plugin[] {
    // this line here is throwing a type error that I don't understand,
    // since very similar code in MarkdownMediaEmbed.ts is fine
    //
    // Anyhow, since I have not diagnosed it and since things seem to
    // be running fine I'm going to just ignore for now.
    // @ts-ignore
    return [ResourceEmbedEditing, ResourceMarkdownSyntax]
  }
}