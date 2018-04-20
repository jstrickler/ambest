// your javascript goes here
$(document).ready(function() {
  $.get("/api/v1/hero/1").success(function (data) {
      $("#hero").html("<h1>apiv1.js</h1>");
      console.log(data);
    }
  );
});
