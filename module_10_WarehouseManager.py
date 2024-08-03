import multiprocessing
class WarehouseManager:
    def __init__(self):
        self.data = multiprocessing.Manager().dict()
    def process_request(self, request):
        if type(request)==tuple and len(request)==3 and type(request[2])==int and type(request[0])==str and type(request[1])==str:
            make = request[1]
            prod = request[0]
            count = request[2]
            if make=='receipt':
                if self.data.get(prod):
                    self.data[prod] += count
                else:
                    self.data[prod] = count

            elif make=='shipment' and self.data.get(prod) and self.data[prod]>0:
                if self.data[prod]>=count:
                    self.data[prod] -= count
                else:
                    self.data[prod]=0

    def run(self,vrequests):

        procs = []
        for vreq in vrequests:
            prc = multiprocessing.Process(target=self.process_request, args=(vreq,))
            procs.append(prc)
            prc.start()
        [proc.join() for proc in procs]




if __name__=='__main__':
    WManager= WarehouseManager()
    requests = [("product1", "receipt", 100),
        ("product2", "receipt", 150),
        ("product1", "shipment", 30),
        ("product3", "receipt", 200),
        ("product2", "shipment", 50)]


    WManager.run(requests)
    print(WManager.data)
