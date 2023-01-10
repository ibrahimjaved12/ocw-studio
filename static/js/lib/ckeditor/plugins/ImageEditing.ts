// abbreviation/abbreviationediting.js

import Plugin from '@ckeditor/ckeditor5-core/src/plugin';

export default class ImageEditing extends Plugin {
    init() {
        this._defineSchema();	
        this._defineConverters();							
    }

    _defineSchema() {											
        const schema = this.editor.model.schema;

        schema.extend( '$text', {
            allowAttributes: [ 'img' ]
        } );
    }

    _defineConverters() {									
        const conversion = this.editor.conversion;

        conversion.for( 'downcast' ).attributeToElement( {
            model: 'img',
            view: ( modelAttributeValue:any, conversionApi:any ) => {
                const { writer } = conversionApi;
                return writer.createAttributeElement( 'img', {
                    src: modelAttributeValue
                } );
            }
        } );
        // Conversion from a view element to a model attribute.
        conversion.for( 'upcast' ).elementToAttribute( {
            view: {
                name: 'img',
                attributes: [ 'src' ]
            },
            model: {
                key: 'img',
                value: viewElement => {
                    const img = viewElement.getAttribute( 'src' );
                    return img;
                }
            }
        } );
    }
}