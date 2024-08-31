<!DOCTYPE html>

<html>
	<head>
		<meta name="description" content="个人博客，记录一些生活和感想"/>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
		<link href="/css/style.css" type="text/css"
		rel="stylesheet" />
		<title>叫渡鸦的少年</title>
	</head>

	<div class="bg">
	
	<body>
		<!-- 标题 -->
		<div class="header">
			
			<a href="/index.html">
				<img src="img/logo.jpg" alt="叫渡鸦的少年" id="logo">
				<h1>
					|叫渡鸦的少年
				</h1>
			</a>
			
		</div>
		
		<!-- 导航栏 -->
			<div>
				<ul id="menu1">
					<li><a href="/articles/essay-index.html">随笔</a></li>
					<li><a href="/articles/daydream.html">诗和远方</a></li>
					<li><a href="/about.html">关于</a></li>
					<li><a href="/contact.html">联系</a></li>
				</ul>
			</div>

		<!--分隔符-->
		<div class="hline1"></div>

		<!--正文-->
		<div class="container1">
			<h2>
				联系
			</h2>
			<?php
				header("Content-Type:text/html; charset=utf-8");

				$servername = "localhost";
				$username = "XXXXXXXX";
				$pswd = "XXXXXXXX";
				$dbname = "XXXXXXX";
				$conn = new mysqli($servername, $username, $pswd, $dbname);
				mysqli_set_charset($conn, 'utf8');
				if($conn->connect_error) {
					die("connect error: " . $conn->connect_error);
				}


				$sql = $conn->prepare("INSERT INTO message (ID, feedback) VALUES
					(?, ?)");
				$sql->bind_param("ss", $fbdate, $feedback);

				$fbdate = date('D, d M Y H:i:s');
				$feedback = $_REQUEST['feedback'];

				if ($sql->execute() === TRUE) {
			    $msg= "谢谢！你的留言已经收到了，有时间我会仔细阅读:)";
			}
				else {
			    echo "发生错误";
			}
			?>
			<p><?php
					echo $msg;
				?>
			</p>

		</div>

		<!--页脚-->
		<div class="footer">
			<div class="menu2" id="first">
				<a href="/index.html">首页</a></div>
			<div class="menu2">
				<a href="/articles/essay-index.html">随笔</a></div>
			<div class="menu2">
				<a href="/articles/daydream.html">诗和远方</a>
					<ul id="menu2list">
						<li class="other"><a href="articles/poems.html" class="sublist">诗</a></li>
						<li class="other"><a href="articles/novel.html" class="sublist">小说</a></li>
					</ul></div>
			<div class="menu2">
				<a href="/about.html">关于</a></div>
			<div class="menu2">
				<a href="/contact.html">联系</a></div>
			<div><img src="img/logo.jpg" id="logobottom"></div>
		</div>

	</body>

</html>


