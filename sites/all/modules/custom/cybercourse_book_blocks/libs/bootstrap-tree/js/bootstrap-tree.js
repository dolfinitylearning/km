(function($) {


  $(document).ready(function() {
    $('.tree > ul').attr('role', 'tree').find('ul').attr('role', 'group');
    $('.tree').find('li:has(ul)').addClass('parent_li').attr('role', 'treeitem')
        .find(' > span').attr('title', 'Collapse this branch').on('click',
           function(e) { 
             var $this = $(e.currentTarget);
             $this.bookBlockMenuClicked( $this ); 
             e.stopPropagation();
           } );
    
    $.fn.bookBlockMenuClicked = function( $this ) {
      if ( ! $this ) {
        $this = this;
      }
      var children = $this.parent('li.parent_li').find(' > ul > li');
      if ( children.hasClass('open') ) {
//      if (children.is(':visiblise')) {
        children.removeClass('open').addClass('closed');
        children.hide('fast');
        $this.attr('title', 'Expand this branch').find(' > i')
            .addClass('icon-plus-sign')
            .removeClass('icon-minus-sign');
      }
      else {
        children.removeClass('closed').addClass('open');
        children.show('fast');
        $this.attr('title', 'Collapse this branch').find(' > i')
              .addClass('icon-minus-sign')
              .removeClass('icon-plus-sign');
      }
    };
    
    //Set classes to show that everything is open initially.
    $(".tree li.parent_li").removeClass('closed').addClass('open');
    
    //Collapse everything.
    $(".tree li.parent_li > span").each(function(){
      $(this).bookBlockMenuClicked();
    });
    
    //Find the menu item that is active, i.e., is the link to the current page.
    var active = $(".tree li.active > span");
    if ( active.length > 0 ) {
      //Show it is on the active path.
//      active.addClass("active-path");
      var reachedMenuTop = false;
      var foundParent = false;
      while ( ! reachedMenuTop ) {
        foundParent = false;
        while ( ! foundParent ) {
          active = active.parent();
          foundParent = ( active.hasClass("menuTop") || active.hasClass("parent_li"));
        }
        if ( active.hasClass("menuTop") ) {
          reachedMenuTop = true;
        }
        else {
          active = active.children("span");
          active.addClass("active-path");
          active = active.closest("li.parent_li");
        }
      }
      //Expand all the menu items on the active path.
      $(".tree .active-path").each(function(){
        $(this).bookBlockMenuClicked();
      });
    }
  });

}(jQuery));
