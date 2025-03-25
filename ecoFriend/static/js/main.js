const base_url = 'http://127.0.0.1/';

function validate(keys, formData){
  if(keys == '' || keys == null || keys == undefined || formData == '' || formData == null || formData == undefined){
    swal(
      'Please fill the required filds!',
      'You have not filled the mandatory filds. Please fill those field to continue.',
      'warning'
    );
    return false;
  }

  for(let key of keys){
    if(document.getElementById(key).hasAttribute('required')){
      if(formData.get(key) == ''){
        swal(
          "Oops! you missed the "+key+" field!",
          "Please fill the required fields carefully.",
          "warning"
        );
        return false;
      }
    }
  }

  return true;
}

const login = function (formId) {
  if(formId == '' || formId == null || formId == undefined){
    swal(
      'Missing Credentials!',
      "Please enter valid credentials to continue.",
      'error'
    );

    return false;
  }

  let formData = new FormData(document.getElementById(formId));

  if(validate(formData.keys, formData)){
    $.ajax({
      url: base_url+'login/',
      data: formData,
      type: 'post',
      processData: false,
      contentType: false,
      success: function (response){
        alert(response);
      },
      error: function(msg){
        alert(msg);
      }
    });
  }
}