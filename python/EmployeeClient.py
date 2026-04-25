from __future__ import print_function
import logging

import grpc
import EmployeeService_pb2
import EmployeeService_pb2_grpc

import const

def prints(op, response, aux=0):
    textos = [
        [f'Employee\'s data by id {aux}: \n' + str(response)], #0
        [f'Updated salary employee from id {aux}\n' + str(response)], #1
        [f'Employee\'s salary from id {aux}: ' + str(response)], #2
        ['Added new employee' + str(response)], #3
        [f'Updated title employee id {aux} ' + str(response)], #4
        [f'Deleted employee id {aux} ' + str(response)], #5
        ['All employees: \n' + str(response)], #6
        [f'All {aux}: \n{str(response)}'] #7
    ]
    print(textos[op][0])

def run():
    with grpc.insecure_channel(const.IP+':'+const.PORT) as channel:
        stub = EmployeeService_pb2_grpc.EmployeeServiceStub(channel)

        # Query an employee's data
        exemplo = 101
        print(f'----------- Buscando o funcionário de id {exemplo} -------------')
        response = stub.GetEmployeeDataFromID(EmployeeService_pb2.EmployeeID(id=exemplo))
        prints(0, response, exemplo)
        
        # promovendo alguem
        exemplo = 101
        print(f'----------- Promovendo funcionário de id {exemplo} -------------')
        response = stub.PromoteEmployee(EmployeeService_pb2.PromoteRequest(id=exemplo, increase=0.1))
        prints(1, response, exemplo)

        #buscando salario
        exemplo = 101
        print(f'----------- Buscando salário do funcionário de id {exemplo} -------------')
        response = stub.GetSalaryByID(EmployeeService_pb2.EmployeeID(id=exemplo))
        prints(2,response,exemplo)

        # Add a new employee
        exemplo = 301
        print(f'----------- Adicionando novo funcionario de id {exemplo} -------------')
        response = stub.CreateEmployee(EmployeeService_pb2.EmployeeData(id=301, name='Jose da Silva', title='Programmer', salary=5000))
        prints(3,response)
        
        # Promovendo um funcionario
        exemplo = 301
        print(f'----------- Promovendo funcionario de id {exemplo} -------------')
        response = stub.PromoteEmployee(EmployeeService_pb2.PromoteRequest(id=exemplo, increase=0.1))
        prints(1,response,exemplo)

        # Criando funcionarios
        print(f'----------- Adicionando novos funcionarios de diversos id\'s -------------')
        response = stub.CreateEmployee(EmployeeService_pb2.EmployeeData(id=401, name='Thiago', title='Programmer', salary=5000))
        prints(3,response)
        
        response = stub.CreateEmployee(EmployeeService_pb2.EmployeeData(id=501, name='Ricardo', title='Programmer', salary=6000))
        prints(3,response)
        
        response = stub.CreateEmployee(EmployeeService_pb2.EmployeeData(id=601, name='Lucas', title='Programmer', salary=7000))
        prints(3,response)

        # Trocando cargo de um funcionario
        exemplo = 301
        print(f'----------- Trocando cargo do funcionario de id {exemplo} -------------')
        response = stub.UpdateEmployeeTitle(EmployeeService_pb2.EmployeeTitleUpdate(id=exemplo, title='Senior Programmer'))
        prints(4, response, exemplo)

        # Deletando um funcionario
        exemplo = 201
        print(f'----------- Deletando o funcionario de id {exemplo} -------------')
        response = stub.DeleteEmployee(EmployeeService_pb2.EmployeeID(id=exemplo))
        prints(5, response, exemplo)

        # Listando todos os funcionarios
        print(f'----------- Listando todos os funcionarios -------------')
        response = stub.ListAllEmployees(EmployeeService_pb2.EmptyMessage())
        prints(6,response)
        
        # Listando todos os funcionarios de determinado cargo
        cargo = 'Programmer'
        print(f'----------- Listando todos os {cargo} -------------')
        response = stub.ListEmployeesByTitle(EmployeeService_pb2.TitleRequest(title=cargo))
        prints(7, response, cargo)


if __name__ == '__main__':
    logging.basicConfig()
    run()