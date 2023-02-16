import ButtonView from "@ckeditor/ckeditor5-ui/src/button/buttonview"

import Plugin from '@ckeditor/ckeditor5-core/src/plugin';

export default class ImageUI extends Plugin {
    init(): void {
        const editor = this.editor;

        editor.ui.componentFactory.add( 'img', () => {
            const button = new ButtonView();
            button.set({
                label:    "img",
                withText: true,
                tooltip: true
              })
            this.listenTo( button, 'execute', () => {
                const src = 'https://pbs.twimg.com/media/E4OzGLfX0AoMeuD.jpg';
                editor.model.change( (writer:any) => {
                    editor.model.insertContent(
                        // Create a text node with the img attribute.
                        writer.createText('img',{ img: src } )
                    );
                } );
            } );

            return button;
        } );
    }
}
