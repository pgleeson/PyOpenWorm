import openworm

# Grabs the representation of the neuronal network
net = openworm.Network()
print(net.aneuron('AVAL').type())

#show how many gap junctions go in and out of AVAL
print(net.aneuron('AVAL').GJ_degree())
