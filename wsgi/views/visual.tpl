<html>
    <head>
        <title>Falling Detection</title>
        <!--Bootstrap-->
        <link rel="stylesheet" type="text/css" href= "{{ get_url('static', filename='bootstrap.css') }}">    
    </head>
    <body>
    <div class="row">
        <div class="span8">
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
                    <td>{{queda.dataEnvio}}</td>
                    <td>{{queda.dataRecebido}}</td>
                    <td><span class="label label-important">{{queda.msg}}</span></td>
                </tr>
                %end
                </tbody>
            </table>
        </div>
    </div>
    </body>
</html>