<template>
	<div class="logo">
		<div class="container">
			<img src="@/assets/logo.svg" alt="" />
			<div class="text">
				<div class="master">Search</div>
				<div class="slug">
			
					<div class="Alpha">Alpha</div>
				</div>
			</div>
		</div>
	</div>
</template>

<style lang="less" scoped>
.logo {
	margin-top: 1.6rem;
	margin-bottom: 0.2rem;
	display: flex;
	.container {
		margin: auto;
		display: flex;
		img {
			height: 1rem;
			width: 1rem;
		}
		.text {
			.master {
				font-size: 0.5rem;
				font-style: italic;
				font-weight: 900;
			}
			.slug {
				font-size: 0.2rem;
				height: 0.2rem;
				position: relative;
				.Alpha{
					position: absolute;
					top: 0;
					right: 0.1rem;
					background-color: rgb(255, 102, 14);
					border-radius: 0.1rem;
					font-size: 0.13rem;
					padding: 0 0.05rem 0 0.05rem;
					font-weight: 900;
				}
			}
		}
	}
}
</style>
