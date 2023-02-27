        new Vue({
            el: '#tests',
            data: {
                quizes: [],
                selected: '',
            },
        created: function () {
            const vm = this;
            axios.get('/api/tests')
                .then(function(response){
                    vm.quizes = response.data
                })
            }
        })
