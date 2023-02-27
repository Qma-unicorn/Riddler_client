new Vue({
    el: '#app',
    data: {
        orders: [],
    },
    created: function () {
        const vm = this;
        axios.get('/api/')
            .then(function(response){
                vm.orders = response.data
            })
    }
}
)