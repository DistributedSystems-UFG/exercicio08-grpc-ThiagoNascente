[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/s_Vw1dfl)
# gRPC-WS-Example

## Actions
> sucessão de passos

```bash
sudo apt install python3-pip
```

```bash
cd /mnt/efs/fs1
```

```bash
sudo git clone https://github.com/DistributedSystems-UFG/exercicio08-grpc-ThiagoNascente.git
```

```bash
cd
```

```bash
sudo chown -R ubuntu:ubuntu /mnt/efs/fs1/exercicio08-grpc-ThiagoNascente
```

```bash
cd exercicio08-grpc-ThiagoNascente/
```

```bash
cd /mnt/efs/fs1/exercicio08-grpc-ThiagoNascente/
```

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

```bash
python3 -m pip install --upgrade pip
```

```bash
python3 -m pip install grpcio
```

```bash
python3 -m pip install grpcio-tools
```

## da maquina servidor
> estando na venv, e no diretorio python/
```bash
python3 -m grpc_tools.protoc -I../protos --python_out=. --grpc_python_out=. ../protos/EmployeeService.proto
```

```bash
python3 EmployeeService.py
```
## de alguma maquina cliente
> estando na venv, e no diretorio python/
```bash
python3 EmployeeClient.py
```

### Note: open port 50051 on the firewall at EC2 (security group)
