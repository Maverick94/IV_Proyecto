# Require the Azure provider plugin
require 'vagrant-azure'

# Create and configure the Azure VMs
Vagrant.configure('2') do |config|

  # Use dummy Azure box
  config.vm.box = 'azure-dummy'

  # Specify SSH key
  config.ssh.private_key_path = '~/.ssh/id_rsa'

  # Configure the Azure provider
  config.vm.provider 'azure' do |az, override|
    # Pull Azure AD service principal information from environment variables
    az.tenant_id = ENV['AZURE_TENANT_ID']
    az.client_id = ENV['AZURE_CLIENT_ID']
    az.client_secret = ENV['AZURE_CLIENT_SECRET']
    az.subscription_id = ENV['AZURE_SUBSCRIPTION_ID']

    # Specify VM parameters
    az.vm_name = 'aztestmaverick'
    az.vm_size = 'Standard_B1s'
    az.vm_image_urn = 'Canonical:UbuntuServer:16.04-LTS:latest'
    az.resource_group_name = 'vagrant'
  end # config.vm.provider 'azure'
  config.vm.provision "ansible" do |ansible|
    ansible.sudo = true
    ansible.playbook = "./provision/playbook.yml"
    ansible.verbose = "-vvvv"

    ansible.host_key_checking = false
  end # config.vm.proviosion
end # Vagrant.configure
