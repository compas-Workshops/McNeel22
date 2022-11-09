from compas.rpc import Proxy
from ghpythonlib.componentbase import executingcomponent as component


class CompasAssemblyInterfacesComponent(component):
    def RunScript(self, assembly, nmax, tmax, amin):
        tmax = tmax or 0.001
        amin = amin or 0.001

        if assembly:
            proxy = Proxy("compas_assembly.algorithms")
            assembly = proxy.assembly_interfaces(assembly, nmax=int(nmax), tmax=tmax, amin=amin)
            self.Message = str(assembly)
            return assembly
        else:
            self.Message = "Select an assembly"
