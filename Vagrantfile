# Require the Azure provider plugin
require 'vagrant-azure'

# Create and configure the Azure VMs
Vagrant.configure('2') do |config|

  # Use dummy Azure box
  config.vm.box = 'azure-dummy'
  config.vm.network "private_network",ip: "192.168.11.4", virtualbox__intnet: "vboxnet0" #Ip privada
  config.vm.hostname = "localhost"

  config.vm.network "forwarded_port", guest: 80, host: 80



  # Configure the Azure provider
  config.vm.provider 'azure' do |az, override|
    # Specify SSH key
    config.ssh.private_key_path = '~/.ssh/id_rsa'

    # Pull Azure AD service principal information from environment variables
    az.tenant_id = ENV['AZURE_TENANT_ID']
    az.client_id = ENV['AZURE_CLIENT_ID']
    az.client_secret = ENV['AZURE_CLIENT_SECRET']
    az.subscription_id = ENV['AZURE_SUBSCRIPTION_ID']


    # az.vm_size = 'Basic_A0' #Tamaño (recursos) de la MV
    # az.location = 'westeurope'
    az.tcp_endpoints = '80'
    # Specify VM parameters
    az.vm_name = 'botactividadesetsiit'
    az.vm_size = 'Standard_B1s'
    az.vm_image_urn = 'Canonical:UbuntuServer:16.04-LTS:latest'
    az.resource_group_name = 'vagrant'
  end # config.vm.provider 'azure'
  config.vm.provision "ansible" do |ansible|
    ansible.force_remote_user = true
    ansible.playbook = "./provision/playbook.yml"
    ansible.host_key_checking=false
    ansible.verbose = "-vvvv"

  end # config.vm.proviosion
end # Vagrant.configure
