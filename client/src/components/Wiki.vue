<template>
  <div class="mytab">
           <el-tabs v-model="type" :stretch="strech">
             <el-tab-pane label="Wiki Search" name="Advanced">
                 <div class="myblock search">
                     <div class="searchblock">
                         <el-input v-model="query" placeholder="Search in wiki"></el-input>
                         <el-button style="margin-left:1.2vw;" type="primary" @click="search":disabled="!query">Search</el-button>
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

      <dl v-html="brightKeyword3(cleantext(this.html))">{{brightKeyword3(cleantext(this.html))}}</dl>







     </div>
</div>




</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            items: [],
            use_time: 0,
            total_count:0,
            string: null,
            data: null,
            body: "",
            query: "123",
            strech: true,
            algo: "tf-idf",
            loading: false,
            page: 1,
            type: "Advanced",
            choosed_algo: "",
            pagesize: 4,
            currpage: 1,
            currentPage1: 1,
            docid:0,
            html:null,
        };
    },

    async mounted() {
        this.algo = this.$route.query.algo;
        this.query = this.$route.query.query;

    },

  methods: {

    search() {
     this.$router.push(
         `/result?query=${this.query}&algo=${
             this.algo
         }`
     );
     const path = 'http://localhost:5000/Results';
     axios.get(path,{params: {query: this.query,algo:this.algo}})
       .then((res) => {
        this.items = res.data.items;
        this.total_count = res.data.total_count;
        this.use_time = res.data.use_time;
        this.choosed_algo = res.data.algo;
       })
       .catch((error) => {
         // eslint-disable-next-line
         console.log(error);
       });
     },

    getwiki() {
      const path = 'http://localhost:5000/Wiki';
      axios.get(path,{params: {docid:this.$route.query.docid}})
        .then((res) => {
          this.html = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
        brightKeyword2(html);
    },
    brightKeyword2(val) {

      let keyword = this.query   //获取输入框输入的内容
      if (val.indexOf(keyword) !== -1 &&keyword.length>=3) {  //判断这个字段中是否包含keyword
        //如果包含的话，就把这个字段中的那一部分进行替换成html字符
        return val.replace(new RegExp(keyword,'ig'), `<font color='#ff0004'>${keyword}</font>`)
      } else {
        return val
      }
    },

    brightKeyword3(val) {

      let keyword = this.query   //获取输入框输入的内容
      const words = keyword.split(' ');
      for(let x = 0; x< words.length; x ++){
        if (words[x].length >=3)
          val = val.replace(new RegExp(words[x],'ig'), `<font color='#ff0004'>${words[x]}</font>`)
      }
        return val
    },


    cleantext(html) {
         return html.replace(new RegExp("href=",'g'), ``)


    },
  },
  created() {
    this.getwiki();
  },
};
</script>




<style>
  .text {
      font-size: 14px;
    }

    .item {
      padding: 18px 0;
    }

    .box-card {
      width: 480px;
    }
.el-tabs__item {
    color: white;
    font-size: 15px;
    font-weight: bold;
}
.el-radio {
    color: black;
}
.el-tabs__header {
    margin: 0 !important;
}
</style>
<style lang="less" scoped>
.pag {
    position: relative;
    margin: 0 auto 50px;
    width: 1000px;
    text-align: center;
    background: transparent !important;
}
.logo {
    position: relative;
    text-align: center;
    margin: 2vh auto 0;
    width: 300px;
    height: 71px;
    img {
        position: absolute;
        left: 0;
        top: 0;
        height: 100%;
        width: 100%;
        display: block;
    }
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
        // align-self: center;
        margin: 20px 0 10px;
    }
    .searchblock {
        display: flex;
    }
}
.cardtitle {
    position: relative;
    color: white;
    font-size: 16px;
    font-weight: bold;
    width: 860px;
    margin: 30px auto 10px;
}
.question {
    font-weight: bold;
    font-size: 22px;
    margin-left: 20px;
    margin-bottom: 10px;
}
.limit-length {
    width: 750px;
    word-break: break-all;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
}
.line-limit-length {
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    width: 750px;
}
.questioninfo {
    margin-left: 20px;
    .box {
        font-weight: bold;
        color: #e69c37;
        margin-right: 9px;
    }
}


.answers {
    margin-left: 20px;
    .box {
        font-weight: bold;
        color: #7ebe50;
        margin-right: 9px;
    }
}
.more {
    margin-left: 20px;
    font-weight: bold;
    color: #569ef8;
}
.clickmore {
    margin-top: 5px;
    text-align: right;
    margin-right: 50px;
}
.text {
    font-size: 14px;
}

.item {
    padding: 18px 0;
}

.box-card {
    width: 860px;
    margin: 0.7vw auto;
    text-align: left;
}
.cards {
    position: relative;
    text-align: center;
    margin: 0 auto 2vw;
    width: 860px;
    display: flex;
    flex-direction: column;
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

    }
}
.el-table{
text-align: center;
    margin: 1vh auto;
    width: 600px;
}
</style>
