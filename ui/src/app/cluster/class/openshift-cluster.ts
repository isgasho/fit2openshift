import {Cluster} from './cluster';

export class OpenshiftCluster extends Cluster {
  auth: string;
  storage: string = null;
}
