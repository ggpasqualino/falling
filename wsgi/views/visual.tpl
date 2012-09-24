<html>
  <head>
    <title>Falling Detection</title>
    <link href='http://fonts.googleapis.com/css?family=Oregano' rel='stylesheet' type='text/css'>
    <style type='text/css'>
      
      body {
        background: #bfdfdf;
      }
      
      #qstframe {
        text-align: center;
        max-width: 300px;
        padding: 2px 2px 12px 2px;
        margin: auto;
				position: relative;
        background: #e9f3f3;
        border-radius: 5px;
        box-shadow: 0px 2px 2px #9cc9c9;
      }
      
	  .qst {
        font-family: 'Oregano', cursive;
        color: #4e9292;
        font-size: 22px;
        margin: 16px 10px 16px 10px;
      }
      
	  .but {
        font-family: sans-serif;
        font-size: 12px;
        font-weight: bold;
        text-height: 16px;
        border: solid 1px;
        border-radius: 2px;
        padding: 4px 12px 4px 12px;
        text-decoration: none;
        background: #c7e0e0;
        border-color: #61a7a7;
        color: #61a7a7;
      }
      
			.sim:hover {
        color: #008800;
        background: #bbee88;
        border-color: #00a800;
      }
      
			.nao:hover {
        color: #880000;
        background: #ef8787;
        border-color: #a80000;
      }
			
			.rst {
				width: 24px;
				height: 24px;
				position: absolute;
				left: 4px;
				bottom: 4px;
				float: left;
				background: url('static/rst.png') no-repeat;
			}
    </style>
  </head>
  <body>
	<table border="1">
            <thead>
                <tr>
                    <th>Data da Queda</th>
                    <th>Data do Recebimento</th>
                    <th>Mensagem</th>
                </tr>
            </thead>
            <tbody>
		%for queda in quedas:
			<tr>
			    <td>{{queda.dataEnvio}}</td>
			    <td>{{queda.dataRecebido}}</td>
			    <td>{{queda.msg}}</td>
			</tr>
		%end
            </tbody>
        </table>
  </body>
</html>