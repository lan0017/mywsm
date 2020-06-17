<template>

  <div class="mytab">
           <el-tabs v-model="type" :stretch="strech">
             <el-tab-pane label="Wiki Search" name="Advanced">
                 <div class="myblock search">
                     <div class="searchblock">
                         <el-input v-model="query" placeholder="Search in wiki"></el-input>
                         <el-button style="margin-left:1.2vw;" type="primary" @click="search" :disabled="!query">Search</el-button>
                     </div>
                     <div class="choose">
                         <el-radio v-model="algo" label="tf-idf">tf-idf</el-radio>
                         <el-radio v-model="algo" label="algorithm2">algorithm2</el-radio>
                         <el-radio v-model="algo" label="algorithm3">algorithm3</el-radio>
                         <el-radio v-model="algo" label="algorithm4">algorithm4</el-radio>
                         <el-radio v-model="algo" label="algorithm5">algorithm5</el-radio>
                     </div>
                 </div>
             </el-tab-pane>
         </el-tabs>


</div>

</template>
<script>



export default {
    data() {
        return {
            type: "Advanced",
            strech: true,
            algo: "tf-idf",
            query: ""
        };
    },

    methods: {
        handleClick(tab, event) {
            console.log(tab, event);
        },
        search() {
            this.$router.push(
                `/result?query=${this.query}&type=${this.type}&algo=${
                    this.algo
                }`
            );
        }
    }
};
</script>

</style>
<style lang="less" scoped>

.el-radio {
    color: black;
}

.mytab {
    text-align: center;
    margin: 1vh auto;
    height: 100px;
    width: 1000px;
}
.myblock {
    display: flex;
    margin-top: 8px;
}
.search {
    flex-direction: column;
    .choose {
        display: flex;
        text-align: center;
        margin: 20px 0 10px;
    }
    .searchblock {
        display: flex;
    }
}

.myapp {
    position: fixed;
    top: 0;
    left: 0;
    height: 100vh;
    width: 100vw;
    img {
        position: absolute;
        left: 0;
        top: 0;
        height: 100%;
        width: 100%;
        display: block;
    }
}
</style>
