import ImageEditing from './ImageEditing';
import ImageUI from './ImageUI';
import Plugin from '@ckeditor/ckeditor5-core/src/plugin';

export default class Image extends Plugin {
    static get requires() {
        return [ ImageEditing, ImageUI ];
    }
}
