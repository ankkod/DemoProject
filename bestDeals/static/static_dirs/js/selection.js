
  $(document).ready(function () {
 
  $('.group').hide();
  $('#deals').show();
  $('#selectMe').change(function () {
    $('.group').hide();
    $('#'+$(this).val()).show();
  })
});
