<!DOCTYPE html>
<html>
<head>
	<title>Update Bill</title>
</head>
<body>
	<div class="bill_print" style="background-color:#dcdcdc; width:300px;">
		<center><h4>Dytila Bill</h4></center>
		<table>
			<tbody>
				<tr>
					<td>Cust ID</td>
					<td>:</td>
					<td>{{ bill_details['_id'] }}</td>
				</tr>
				<tr>
					<td>Bill ID</td>
					<td>:</td>
					<td>{{ bill_id }}</td>
				</tr>
				<tr>
					<td>Name</td>
					<td>:</td>
					<td>{{ bill_details['user_name'] }}</td>
				</tr>
				<tr>
					<td>Food</td>
					<td>:</td>
					<td>{{ bill_details['food_name'] }}</td>
				</tr>
				<tr>
					<td>Location</td>
					<td>:</td>
					<td>{{ bill_details['location'] }}</td>
				</tr>
			</tbody>
		</table>
		{{ bill_details['meal_freq'] }} meals remaining
	</div>
	<?php
				header("Content-Type: application/vnd.msword");
				header("Expires: 0");
				header("Cache-Control: must-revalidate, post-check=0, pre-check=0");
				header("content-disposition: attachment;filename=dytila.doc");		
	  ?>
</body>
</html>
