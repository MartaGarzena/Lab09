from model.model import Model

model = Model()
model.buildGraphPesato()
print("Num nodi:", model.getNumNodi())
print("Num archi:", model.getNumArchi())

archiMaggiori = model.getArchiPesoMaggiore(4502.0000)
for a in archiMaggiori:
    print(a)
