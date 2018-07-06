import yaml

from charms.reactive import set_flag
from charms.reactive import when_not

from charms import layer
from charms.layer.basic import pod_spec_set


@when_not('charm.kubeflow-tf-job-dashboard.started')
def start_charm():
    layer.status.maintenance('configuring tf-job-dashboard container')

    pod_spec_set(yaml.dump({
        'containers': [
            {
                'name': 'tf-job-dashboard',
                'image': ('gcr.io/kubeflow-images-public/'
                          'tf_operator:v20180329-a7511ff'),
                'command': [],
                'ports': [
                    {
                        'name': 'tf-dashboard',
                        'containerPort': 8080,
                    },
                ],
            },
        ],
    }))

    layer.status.active('ready')
    set_flag('charm.kubeflow-tf-job-dashboard.started')
