var updateBtns = document.getElementsByClassName('update-cart');
var csrftoken = getToken('csrftoken');
for (var i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId: ', productId, 'action: ', action)
        console.log(csrftoken)
        updateOrder(productId, action)
    })
}

function updateOrder(productId, action){
    console.log("User is logged in, sending data...")
    var url = "/store/update_order/"
    console.log(url)
    fetch(url, {
        method: "POST",
        headers: {
            "Content-Type":"application/json",
            "X-CSRFToken": csrftoken
        },
        body: JSON.stringify(
            {"productId": productId,
            "action": action}
        )
    })
    .then((data) => {
        console.log("data: ",data)
        document.location.reload()

    })
}

function getToken(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i=0; i < cookies.length; i++) {
            cookie = cookies[i].trim();
            if (cookie.substring(0, name.length+1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
