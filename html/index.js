$("#nameForm").submit(function(e) {

    var url = "/"; // the script where you handle the form input.

    $.ajax({
          method: "POST",
          url: url,
          data: $("#nameForm").serialize(), // serializes the form's elements.
          success: function(data)
          {
              alert(data); // show response from the php script.
          }
        });

    e.preventDefault(); // avoid to execute the actual submit of the form.
    });