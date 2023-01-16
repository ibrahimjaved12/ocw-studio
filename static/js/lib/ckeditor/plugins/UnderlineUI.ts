import ButtonView from '@ckeditor/ckeditor5-ui/src/button/buttonview';
import Plugin from '@ckeditor/ckeditor5-core/src/plugin';

export default class UnderlineBoxUI extends Plugin {
    init() {
        const editor = this.editor;
        const t = editor.t;
        editor.ui.componentFactory.add( 'underline', (locale: any) => {
            const command = editor.commands.get( 'underline' );
            const buttonView = new ButtonView( locale );
            buttonView.set( {
                label: t( 'underline' ),
                withText: true,
                tooltip: true
            } );

            buttonView.bind( 'isOn', 'isEnabled' ).to( command, 'value', 'isEnabled' );

            this.listenTo( buttonView, 'execute', () => {
                editor.execute( 'underline' )
                editor.editing.view.focus();
            } );

            return buttonView;
        } );
    }
}
