url = window.location.href

$('#max_price').keyup(function () {
    min_price = $('#min_price').val()
    max_price = $('#max_price').val()
    if (min_price > max_price)
        console.log(min_price, max_price)
})

$('.price-filter').click(function () {
    min_price = $('#min_price').val()
    max_price = $('#max_price').val()
    console.log(min_price, max_price)
    new_url = set_params(url, 'min-price', min_price)
    new_url = set_params(new_url, 'max-price', max_price)
    window.location.replace(new_url)
})

$('.sorting').change(function () {
    new_url = set_params(url, 'sorting', $(this).val())
    console.log(new_url)
    window.location.replace(new_url)
})

$('.per-page').change(function () {
    new_url = set_params(url, 'per-page', $(this).val())
    console.log(new_url)
    window.location.replace(new_url)
})
$('.paging').click(function () {
    new_url = set_params(url, 'page', $(this).data('value'))
    console.log(new_url)
    window.location.replace(new_url)
})
$('.select-category').click(function () {
    new_url = set_params(url, 'cat', $(this).data('category'))
    console.log(new_url)
    window.location.replace(new_url)
})

function set_params(url, param, value) {
    path = url.split('?')[0]
    if (url.includes("?")) {
        curl = url.split('?')[1]
        params = curl.split('&')
        console.log(params)
        is_found = false
        for (i = 0; i < params.length; i++) {
            if (params[i].split('=')[0] == param) {
                params[i] = `${param}=${value}`
                is_found = true
            }
        }
        curl = params.join('&')
        if (!is_found)
            curl += `&${param}=${value}`
        url = path + '?' + curl
    } else {
        curl = `?${param}=${value}`
        url = path + curl
    }

    return url
}

//    ADD TO CART
$('.add-cart').click(function () {
    product_id = $(this).data('id')
    data = {'product_id': product_id}
    url_add_cart = '/order/add-cart/'
    post_data(url_add_cart, data, update_badge)

})

function update_badge(response) {
    $('#badge').text(response.items_count)
    if (response.event == 'added') {
        $(`#pbtn${response.pid}`).removeClass('btn-primary')
        $(`#pbtn${response.pid}`).text('Added to cart')
        $(`#pbtn${response.pid}`).addClass('btn-success')
    }else if(response.event == 'deleted'){
        $(`#pbtn${response.pid}`).removeClass('btn-success')
        $(`#pbtn${response.pid}`).text('Add to cart')
        $(`#pbtn${response.pid}`).addClass('btn-primary')
    }

}

function post_data(url, data, callback) {
    $.ajax({
        type: "POST",
        url: url,
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        data: JSON.stringify(data),
        success: callback
    })
}

// END  ADD TO CART

$('.change-quantity').click(function () {
    item_id = $(this).data('item')
    action = $(this).data('action')
    let url_change_quantity = '/order/change-quantity/'
    let data = {
        'item': item_id,
        'action': action
    }
    post_data(url_change_quantity, data, item_quantity_cange)
})

$('.input-quantity').keyup(function () {
    value = $(this).val()
    item_id = $(this).data('item')
    action = 'onkeyup'
    console.log(value, item_id)
    let url_change_quantity = '/order/change-quantity/'
    let data = {
        'item': item_id,
        'action': action,
        'value': value
    }
    post_data(url_change_quantity, data, item_quantity_cange)
})

function item_quantity_cange(response) {
    // console.log(response)
    if (response.error == false) {
        $(`#${response.item}`).val(response.item_quantity)
        $(`#price${response.item}`).text(`$${response.total_price}.0`)
        $('#total-price').text(`$${response.total}.0`)
    }
}

$('.remove-item').click(function () {
    item_id = $(this).data('id')
    console.log(item_id)
    $.ajax({
        type: "GET",
        url: `/order/remove/${item_id}/`,
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        success: function (response) {
            console.log(response)
            if (response.success)
                $(`#item_tr_${response.id}`).remove()
            $('#badge').text(response.items_count)
            $('#total-price').text(`$${response.total}.0`)
        }
    })
})

