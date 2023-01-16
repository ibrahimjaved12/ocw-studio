import Plugin from '@ckeditor/ckeditor5-core/src/plugin';
import { editor } from "@ckeditor/ckeditor5-core"
import UnderlineCommand from './UnderlineCommand';

export default class UnderlineEditing extends Plugin {
    constructor(editor: editor.Editor) {
      super(editor);
    }
  
    init() {
      const editor = this.editor;
      editor.model.schema.extend( '$text', { allowAttributes: 'underline' } );
      editor.model.schema.setAttributeProperties( 'underline', {
        isFormatting: true,
        copyOnEnter: true
      } );
      editor.conversion.attributeToElement( {
        model: 'underline',
        view: 'u',
        upcastAlso: [
          'u',
          (          viewElement: { getStyle: (arg0: string) => any; }) => {
            const textDecoration = viewElement.getStyle( 'text-decoration' );
            console.log(textDecoration)
            if ( !textDecoration ) {
              return null;
            }
  
            if ( textDecoration.includes('underline') ) {
              return {
                name: true,
                styles: [ 'text-decoration' ]
              };
            }
          }
        ]
      } 
      );
     
      this.editor.commands.add('underline', new UnderlineCommand(this.editor));
      editor.keystrokes.set( 'CTRL+U', 'underline' );

    }
  }
