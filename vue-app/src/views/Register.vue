<template>
	<div class="register">
		<template>
			<div class="login-wrap">
				<el-form class="login-container">
					<h1 class="title">学长工具库注册</h1>
					<el-form-item label="">
						<el-input
							type="text"
							v-model="username"
							placeholder="注册账号"
							autocomplete="off"
						></el-input>
					</el-form-item>
					<el-form-item label="">
						<el-input
							type="password"
							v-model="password"
							placeholder="注册密码"
							autocomplete="off"
						></el-input>
					</el-form-item>
					<el-form-item>
						<el-button type="primary" style="width: 100%" @click="doSubmit()"
							>提交</el-button
						>
					</el-form-item>
					<el-row style="text-align: center; margin-top: -10px">
						<el-link type="primary" @click="gotoLogin()">用户登陆</el-link>
					</el-row>
				</el-form>
			</div>
		</template>
	</div>
</template>
<script>
import axios from "axios";
export default {
	name: "RegisterView",
	data() {
		return {
			msg: "Welcome to Your Vue.js App",
			username: "",
			password: "",
		};
	},
	methods: {
		gotoLogin() {
			// 跳转登陆页面
			this.$router.push("/login");
		},
		doSubmit() {
			let url = "http://localhost:8888/server/userRegister";
			//获取数据
			let params = {
				username: this.username,
				password: this.password,
			};

			axios
				.post(url, params)
				.then((r) => {
					console.log(r);
					if (r.data.success) {
						this.$message({
							message: r.data.msg,
							type: "success",
						});
					} else {
						this.$message.error(r.data.msg);
					}
				})
				.catch((e) => {
					console.log(e);
				});
		},
	},
};
</script>
<style lang="" scoped>
/* .login-wrap {
	box-sizing: border-box;
	width: 100%;
	height: 100%;
	padding-top: 10%;
	background-repeat: no-repeat;
	background-position: center right;
	background-size: 100%;
}
.login-container {
	border-radius: 10px;
	margin: 0px auto;
	width: 350px;
	padding: 30px 35px 15px 35px;
	background: #fff;
	border: 1px solid #eaeaea;
	text-align: left;
	box-shadow: 0 0 20px 2px rgba(0, 0, 0, 0.1);
}

.title {
	margin: 0px auto 40px auto;
	text-align: center;
	color: #505458;
} */
</style>
