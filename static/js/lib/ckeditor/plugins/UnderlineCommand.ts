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
        const selection = doc.selection;
        this.isEnabled = model.schema.checkAttributeInSelection( selection, 'underline' );
    }
    execute() {
        const model = this.editor.model;
        const doc = model.document;
        const selection = doc.selection;
    
        model.change( (writer: { removeSelectionAttribute: (arg0: string) => void; setSelectionAttribute: (arg0: string, arg1: boolean) => void; }) => {
            if ( selection.hasAttribute( 'underline' ) ) {
                writer.removeSelectionAttribute( 'underline' );
            } else {
                writer.setSelectionAttribute( 'underline', true );
            }
        });
    }
   
}

