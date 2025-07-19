document.addEventListener("DOMContentLoaded", function () {
  // send comment with enter key
  document.querySelectorAll("form textarea[name='content']").forEach(function (textarea) {
    textarea.addEventListener("keydown", function (e) {
      if (e.key === "Enter" && !e.shiftKey) {
        e.preventDefault();
        var form = textarea.closest("form");
        if (form) {
          form.submit();
        }
      }
    });
  });
});
