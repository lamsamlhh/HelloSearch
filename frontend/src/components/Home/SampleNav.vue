<template>
	<div class="sample-nav">
		<div class="left">
			Search
		</div>
		<div class="right">
			<!-- <svg class="icon" aria-hidden="true" @click="gomore">
				<use xlink:href="#icon-yingyongchengxu"></use>
			</svg> -->
			<router-link class="btn1" :to="{ path: '/login' }">登录</router-link>|
				<router-link class="btn2" :to="{ path: '/register' }">注册</router-link>
		</div>
	</div>
</template>
<script setup>
import { getIP } from "@/api/index.js";
import store from "@/store/index.js";
import { useRouter } from "vue-router";

const router = useRouter();
const avator = getIP() + store.state.UserProfile.avator || "";
function gotouser() {
	router.push({ path: "/userprofile" });
}
function gomore(){
	alert("todo")
}
</script>

<style lang="less" scoped>
.sample-nav {
	display: flex;
	height: 0.45rem;
	justify-content: space-between;
	align-items: center;
	margin-top: 0;
	background-color: #323233;
	.left {
		font-family: "Gill Sans", "Gill Sans MT", Calibri, "Trebuchet MS",
			sans-serif;
		font-style: italic;
		font-size: 0.35rem;
		font-weight: 900;
		background-color: #323233;
		color: #d6d6d6;
		opacity: 0.8;
		margin: 0 0 0 0.1rem;
	}
	.right {
		display: flex;
		justify-content: space-around;
		align-items: center;
		margin: 0 0.15rem 0 0;
		background-color: #323233;
		color: #323233;
		.icon {
			width: 0.25rem;
			height: 0.25rem;
			fill: #d6d6d6;
			margin-right: 0.2rem;
			cursor: pointer;
		}
		.ava {
			height: 0.4rem;
			height: 0.4rem;
			border-radius: 0.4rem;
			cursor: pointer;
			color: #323233;
		}
		.btn1 {
			font-size: 0.15rem;
			margin-right: 0.05rem;
			font-weight: 900;
			background-color: #323233;
			color: #d6d6d6;
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
