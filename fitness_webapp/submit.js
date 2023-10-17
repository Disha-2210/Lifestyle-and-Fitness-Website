<script type="text/javascript">
      function answer()
      {
           var ans = document.getElementsByName('fav_language');

for (var i = 0, length = ans.length; i < length; i++) {
    if (ans[i].checked) {
        if((ans[i].value)=="rare")
        alert("Correct Answer");
        else
          alert("Wrong ANswer");
    }
}
      }
</script>