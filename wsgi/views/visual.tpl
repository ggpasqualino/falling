<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Falling Detection</title>
        <!--Bootstrap-->
        <link rel="stylesheet" type="text/css" href= "{{ get_url('static', filename='bootstrap.css') }}">    
    <meta http-equiv="refresh" content="60">
    </head>
    <body>    
        <div class="container">
            <h1>Sistema para Monitoração de Queda de Idosos</h1>
        </div>
        <div class="container">
            <table class="table table-striped table-bordered">
            <thead>
                <tr>
                <th>Enviado em</th>
                <th>Recebido em</th>
                <th>Pessoa</th>
                <th>Mensagem</th>
                <th>Local Aproximado</th>
                </tr>
            </thead>
            <tbody>
                %for queda in quedas:
                <tr>
                    <td>{{queda.get('dataEnvio')}}</td>
                    <td>{{queda.get('dataRecebido')}}</td>
                    <td>{{queda.get('pessoa')}}</td>
                    <td><span class="label label-important">{{queda.get('msg')}}</span></td>
                    <td><a href="https://maps.google.com.br/maps?q={{queda.get('local')}}">{{queda.get('local')}}</a></td>
                </tr>
                %end
                </tbody>
            </table>
        </div>    
    </body>
</html>