<html>
    <head>
        <title>Falling Detection</title>
        <!--Bootstrap-->
        <link rel="stylesheet" type="text/css" href= "{{ get_url('static', filename='bootstrap.css') }}">    
	<meta http-equiv="refresh" content="60">
    </head>
    <body>    
        <div class="container">
            <table class="table table-striped table-bordered">
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
                    <td>{{queda.get('dataEnvio')}}</td>
                    <td>{{queda.get('dataRecebido')}}</td>
                    <td><span class="label label-important">{{queda.get('msg')}}</span></td>
                </tr>
                %end
                </tbody>
            </table>
        </div>    
    </body>
</html>