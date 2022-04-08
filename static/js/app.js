new Vue({
    el: '#sup_app',
    data: {
        sup: []
    },
    created: function () {
        const vm = this;
        axios.get('/api/suppliers/')
            .then(function (response){
                vm.sup = response.data
            })
    }
})