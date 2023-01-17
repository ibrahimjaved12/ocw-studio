import { editor } from '@ckeditor/ckeditor5-core';
import Command from '@ckeditor/ckeditor5-core/src/command';

export default class UnderlineCommand extends Command {
    editor: any;
    constructor(editor: editor.Editor) {
      super(editor);
      this.editor = editor;
    }
    refresh() {
		const model = this.editor.model;
		const doc = model.document;

		this.value = this._getValueFromFirstAllowedNode();
		this.isEnabled = model.schema.checkAttributeInSelection( doc.selection, 'underline' );
	}

    execute( options = { forceValue: undefined }  ) {
		const model = this.editor.model;
		const doc = model.document;
		const selection = doc.selection;
		const value = ( options.forceValue === undefined ) ? !this.value : options.forceValue;

		model.change( (writer: { setSelectionAttribute: (arg0: any, arg1: boolean) => void; removeSelectionAttribute: (arg0: any) => void; setAttribute: (arg0: any, arg1: boolean, arg2: any) => void; removeAttribute: (arg0: any, arg1: any) => void; }) => {
			if ( selection.isCollapsed ) {
				if ( value ) {
					writer.setSelectionAttribute( 'underline', true );
				} else {
					writer.removeSelectionAttribute( 'underline' );
				}
			} else {
				const ranges = model.schema.getValidRanges( selection.getRanges(), 'underline' );

				for ( const range of ranges ) {
					if ( value ) {
						writer.setAttribute( 'underline', value, range );
					} else {
						writer.removeAttribute( 'underline', range );
					}
				}
			}
		} );
	}
    _getValueFromFirstAllowedNode() {
		const model = this.editor.model;
		const schema = model.schema;
		const selection = model.document.selection;

		if ( selection.isCollapsed ) {
			return selection.hasAttribute( 'underline' );
		}

		for ( const range of selection.getRanges() ) {
			for ( const item of range.getItems() ) {
				if ( schema.checkAttribute( item, 'underline' ) ) {
					return item.hasAttribute( 'underline' );
				}
			}
		}

		return false;
	}
   
}
