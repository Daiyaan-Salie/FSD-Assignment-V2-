<template>
<HeaderCode/>
    <div class="container">
        <p>{{msg}}</p>
    </div>
</template>

<script>
import axios from 'axios'
import HeaderCode from '../components/HeaderCode.vue'
export default {
    name: 'Sectors',
        components: {HeaderCode,
        },
    data() {
        return {
            msg: ""
        };
    },
    methods : {
        getResponse(){
            const path = 'http://localhost:5000/weights';
            axios.get(path)
            .then((res) => {
                console.log(res.data);
                this.msg = res.data;
            })
            .catch ((err) => {
                console.error(err);
            });
        },
    },
    created(){
        this.getResponse();
    }
}


</script>