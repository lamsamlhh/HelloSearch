<template>
  <div class="detail-nav">
    <router-link class="back" :to="{ path: '/' }">
      <div class="logo">
        Search
        <div class="Alpha">Alpha</div>
      </div>
    </router-link>
    <div class="search">
      <search-box-detail></search-box-detail>
    </div>
    <div class="right">
      <!-- <svg class="icon" aria-hidden="true" @click="goset">
				<use xlink:href="#icon-shezhi"></use>
			</svg>
			<svg class="icon" aria-hidden="true" @click="gomore">
				<use xlink:href="#icon-yingyongchengxu"></use>
			</svg> -->
      <!-- <img
				v-if="store.state.UserProfile != ''"
				class="ava"
				:src="avator"
				alt=""
				@click="gotouser"
			/> -->
      <router-link class="btn1" :to="{ path: '/login' }">登录</router-link>
      <router-link class="btn2" :to="{ path: '/register' }">注册</router-link>
      <!-- <router-link class="btn2" :to="{ path: '/' }">HTTP分析</router-link> -->
    </div>
  </div>
</template>
<script>
import SearchBoxDetail from "@/components/ResultList/SearchBoxDetail.vue";

export default {
  components: {
    SearchBoxDetail,
  },
};
</script>
<script setup>
import { getIP } from "@/api/index.js";
import store from "@/store/index.js";
import { useRouter } from "vue-router";

const router = useRouter();
const avator = getIP() + store.state.UserProfile.avator || "";
function gotouser() {
  router.push({ path: "/userprofile" });
}
function gomore() {
  alert("todo");
}
function goset() {
  alert("todo");
}
</script>

<style lang="less" scoped>
.detail-nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.1rem 0.15rem 0.15rem 0.2rem;
  border-bottom: 1px solid #999;
  position: sticky;
  position: -webkit-sticky; // 兼容 -webkit 内核的浏览器
  top: 0px;
  background-color: #323233;
  .logo {
    font-size: 0.3rem;
    font-weight: 900;
    font-style: italic;
    position: relative;
    background-color: #323233;
    color: #d6d6d6;
    .Alpha {
      position: absolute;
      top: 0;
      left: 0.38rem;
      background-color: rgb(255, 102, 14);
      border-radius: 0.1rem;
      font-size: 0.13rem;
      padding: 0 0.05rem 0 0.05rem;
      font-weight: 900;
    }
  }
  .search {
    position: absolute;
    top: 0.1rem;
    left: 1.5rem;
  }
  .right {
    display: flex;
    justify-content: space-around;
    align-items: center;
    background-color: #323233;
    .icon {
      width: 0.25rem;
      height: 0.25rem;
      fill: #222;
      margin-right: 0.2rem;
    }
    .ava {
      height: 0.4rem;
      height: 0.4rem;
      border-radius: 0.4rem;
      cursor: pointer;
    }
    .btn1 {
      font-size: 0.15rem;
      margin-right: 0.05rem;
      font-weight: 900;
      color: #d6d6d6;
      background-color: #323233;
    }
    .btn2 {
      font-size: 0.15rem;
      margin-left: 0.05rem;
      font-weight: 900;
      color: #d6d6d6;
      background-color: #323233;
    }
  }
}
</style>
