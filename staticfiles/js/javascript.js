/* jshint esversion: 6 */
document.addEventListener("DOMContentLoaded", function () {
  // send comment with enter key
  document.querySelectorAll("form textarea[name='content']").forEach(function (textarea) {
    textarea.addEventListener("keydown", function (e) {
      if (e.key === "Enter" && !e.shiftKey) {
        e.preventDefault();
        const form = textarea.closest("form");
        if (form) form.submit();
      }
    });
  });

  // auto-close alerts after 3 seconds (Suggestion from 1:1 Session)
  const alerts = document.querySelectorAll('.alert');
  alerts.forEach(function (alert) {
    setTimeout(function () {
      alert.style.transition = "opacity 0.5s ease";
      alert.style.opacity = "0";

      setTimeout(function () {
        if (alert.parentNode) {
          alert.parentNode.removeChild(alert);
        }
      }, 500);
    }, 3000);
  });
});
