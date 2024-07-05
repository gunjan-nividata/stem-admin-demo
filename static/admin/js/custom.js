//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js'
if (!$) {
    $ = django.jQuery;
}
$(function() {
  $('textarea').froalaEditor({
    pluginsEnabled: ['mathEditor', 'otherPluginsYouNeed'],
    toolbarButtons: ['bold', 'italic', 'underline', 'insertMath', '...'],
    // other Froala configuration options
  });
});