#!/bin/bash
# AWS Managed Services - 2020-05-21
# This will install the AWS Managed Services CLI.
# This includes the:
#  * AWS Managed Services Change Management CLI (amscm)
#  * AWS Managed Services SKMS CLI (amsskms)
# Prerequisites:
#  * Linux or Mac operating systems
#  * AWS CLI Version 1.7.3 or above (The latest version is recommended)

# AWS CLI
# To install the latest version of the AWS CLI, please visit:
#  * https://aws.amazon.com/cli/
# To know the version of the AWS CLI installed on your system, please run:
#  * aws --version

echo "This will install the AWS Managed Services CLI."
echo "The latest AWS CLI is a pre-requisite to install the AWS Managed Services CLI."

echo ""

if [! command -v aws 2>/dev/null ]; then
  echo "You do not have the latest AWS CLI installed."
  echo "To install the latest AWS CLI, please visit"
  echo "  https://aws.amazon.com/cli/"
  echo "After you have installed the latest AWS CLI, please run this script again."
  exit;
fi

echo "We have found the following version of the AWS CLI:"
aws --version
echo ""
echo "If you want to update or re-install the AWS CLI, "
echo "  you can do so by visiting https://aws.amazon.com/cli/"

echo ""

echo "Do you wish to install the AWS Managed Services CLI?"
echo "  Please type the number with the desired option."
select yn in "Yes" "No"; do
  case $yn in
    Yes )
      echo "Proceeding with the installation of the latest AWS Managed Services CLI."

      # Checking directory and files are accessible for this script for amscm.
      amscm_directory="amscm/2020-05-21"
	  if [ ! -d $amscm_directory ]; then
	    echo "ERROR: The $amscm_directory folder is not in the same directory as this script."
	    echo "Exiting the installation."
        exit 1;
      fi

      if [ ! -f "$amscm_directory/service-2.json" ]; then
	    echo "ERROR: The files under $amscm_directory folder do not exist."
	    echo "Exiting the installation."
        exit 1;
      fi

      # Checking directory and files are accessible for this script for amsskms.
      amsskms_directory="amsskms/2020-05-21"
      if [ ! -d $amsskms_directory ]; then
	    echo "ERROR: The $amsskms_directory folder is not in the same directory as this script."
	    echo "Exiting the installation."
        exit 1;
      fi

      if [ ! -f "$amsskms_directory/service-2.json" ]; then
	    echo "ERROR: The files under $amsskms_directory folder do not exist."
	    echo "Exiting the installation."
        exit 1;
      fi

      # Some variables to help the installation
      today_date=$(date +%Y%m%d)
      backup_directory="$HOME/.aws/backup_older_clis/$today_date"

      # Creating the directories to backup the previous AWS Managed Services CLIs.
      mkdir -p $backup_directory

      # Move old versions of the services to $backup_directory.
      echo "Backing up previous AWS Managed Services CLIs under the following directory:"
      echo $backup_directory
      if [ -d "$HOME/.aws/models/mcchangemanagement" ]; then
        cp -r $HOME/.aws/models/mcchangemanagement $backup_directory
        rm -rf $HOME/.aws/models/mcchangemanagement
      fi
      if [ -d "$HOME/.aws/models/mcprovisioning" ]; then
        cp -r $HOME/.aws/models/mcprovisioning $backup_directory
        rm -rf $HOME/.aws/models/mcprovisioning
      fi
      if [ -d "$HOME/.aws/models/amscm" ]; then
        cp -r $HOME/.aws/models/amscm $backup_directory
        rm -rf $HOME/.aws/models/amscm
      fi
      if [ -d "$HOME/.aws/models/amsskms" ]; then
        cp -r $HOME/.aws/models/amsskms $backup_directory
        rm -rf $HOME/.aws/models/amsskms
      fi

      echo ""

      echo "Installing the the latest AWS Managed Services CLI."

      # Create the new directories for AWS Managed Services CLIs.
      mkdir -p $HOME/.aws/models/amscm
      mkdir -p $HOME/.aws/models/amsskms

      # Copy latest version of the services
	  cp -r amscm $HOME/.aws/models
      cp -r amsskms $HOME/.aws/models
      echo "AWS Managed Services CLIs has been installed."

      echo ""

      echo "For usage instructions and examples, please run:"
      echo "  aws amscm help"
      echo "  aws amsskms help"

      break;;

    No )
      echo "You have chosen to not install the AWS Managed Services CLI."
      echo "Aborting installation."
      exit;;

    esac
done