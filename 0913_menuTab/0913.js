$(document).ready(function() {
  var menu = $('.main-menu > li');
  var span = $('.main-menu span');
  var last_item = $('.sub-menu li:last-child a');

  menu.hover(function() {
    $(this).find('.sub-menu').toggleClass('sub-menu-active');
  });
  span.focusin(function() {
    $(this).siblings('.sub-menu').addClass('sub-menu-active');
  });
  last_item.focusout(function() {
    $(this).parents('.sub-menu').removeClass('sub-menu-active');
  });
  //   안됨. 안지워짐 계속 메뉴 겹침
  span.focusout(function() {
    $(this).parents('.sub-menu').removeClass('sub-menu-active');
  });
});