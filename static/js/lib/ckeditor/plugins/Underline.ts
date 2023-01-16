import UnderlineEditing from './UnderlineEditing';
import UnderlineUI from './UnderlineUI';
import Plugin from '@ckeditor/ckeditor5-core/src/plugin';

export default class Underline extends Plugin {
    static get requires() {
        return [ UnderlineEditing, UnderlineUI ];
    }
}
