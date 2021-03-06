from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pages.qci_page import QCIPage


class InstallationProgress(QCIPage):

    # locators
    _overview_tab_loc = (By.XPATH, '//li[contains(@class,"ember-view")]/a[text()="Overview"]')
    _details_tab_loc = (By.XPATH, '//li[contains(@class,"ember-view")]/a[text()="Details"]')
    _log_tab_loc = (By.XPATH, '//li[contains(@class,"ember-view")]/a[text()="Log"]')

    _error_checkbox_loc = (By.XPATH, '//input[@name="error"]')
    _warn_checkbox_loc = (By.XPATH, '//input[@name="warn"]')
    _info_checkbox_loc = (By.XPATH, '//input[@name="info"]')
    _debug_checkbox_loc = (By.XPATH, '//input[@name="debug"]')
    _logs_dropdown_loc = (By.XPATH, '//select[@id="log-file-select"]')

    _progress_bar_class_success_name = 'progress-bar-success'
    _progress_bar_class_error_name = 'progress-bar-danger'
    _progress_bar_all = (By.XPATH, '//div[@role="progressbar"]')

    _progress_bar_satellite_row = (By.XPATH, '//div[@class="ember-view row"]/div[contains(@class, "rhci-review-product-name")]/h3[text()="Satellite"]/../..')
    _progress_bar_satellite = (By.XPATH, '{}//div[@role="progressbar"]'.format(_progress_bar_satellite_row[1]))
    _progress_bar_satellite_label = (By.XPATH, '{}//div[@class="progress-bar-label"]'.format(_progress_bar_satellite_row[1]))

    _progress_bar_rhv_row = (By.XPATH, '//div[@class="ember-view row"]/div[contains(@class, "rhci-review-product-name")]/h3[text()="RHV"]/../..')
    _progress_bar_rhv = (By.XPATH, '{}//div[@role="progressbar"]'.format(_progress_bar_rhv_row[1]))
    _progress_bar_rhv_label = (By.XPATH, '{}//div[@class="progress-bar-label"]'.format(_progress_bar_rhv_row[1]))

    _progress_bar_cloudforms_row = (By.XPATH, '//div[@class="ember-view row"]/div[contains(@class, "rhci-review-product-name")]/h3[text()="CloudForms"]/../..')
    _progress_bar_cloudforms = (By.XPATH, '{}//div[@role="progressbar"]'.format(_progress_bar_cloudforms_row[1]))
    _progress_bar_cloudforms_label = (By.XPATH, '{}//div[@class="progress-bar-label"]'.format(_progress_bar_cloudforms_row[1]))

    _progress_bar_openshift_row = (By.XPATH, '//div[@class="ember-view row"]/div[contains(@class, "rhci-review-product-name")]/h3[text()="OpenShift"]/../..')
    _progress_bar_openshift = (By.XPATH, '{}//div[@role="progressbar"]'.format(_progress_bar_openshift_row))
    _progress_bar_openshift_label = (By.XPATH, '{}//div[@class="progress-bar-label"]'.format(_progress_bar_openshift_row))

    _progress_bar_openstack_row = (By.XPATH, '//div[@class="ember-view row"]/div[contains(@class, "rhci-review-product-name")]/h3[text()="RHOSP"]/../..')
    _progress_bar_openstack = (By.XPATH, '{}//div[@role="progressbar"]'.format(_progress_bar_openstack_row))
    _progress_bar_openstack_label = (By.XPATH, '{}//div[@class="progress-bar-label"]'.format(_progress_bar_openstack_row))

    # Content error locators
    _content_error_container = (By.XPATH, '//div[@class="content-error-container"]')
    _abandon_button = (By.XPATH, '//button[contains(., "Abandon")]')
    _abandon_delete_button = (By.XPATH, '//button[contains(., "Abandon and Delete")]')
    _redeploy_button = (By.XPATH, '//button[contains(., "Redeploy")]')

    # elements
    @property
    def overview_tab(self):
        return self.selenium.find_element(*self._overview_tab_loc)

    @property
    def details_tab(self):
        return self.selenium.find_element(*self._details_tab_loc)

    @property
    def log_tab(self):
        return self.selenium.find_element(*self._log_tab_loc)

    @property
    def error_checkbox(self):
        return self.selenium.find_element(*self._error_checkbox_loc)

    @property
    def warn_checkbox(self):
        return self.selenium.find_element(*self._warn_checkbox_loc)

    @property
    def info_checkbox(self):
        return self.selenium.find_element(*self._info_checkbox_loc)

    @property
    def debug_checkbox(self):
        return self.selenium.find_element(*self._debug_checkbox_loc)

    @property
    def progress_bar_all(self):
        return self.selenium.find_elements(*self._progress_bar_all)

    @property
    def progress_bar_satellite(self):
        return self.selenium.find_element(*self._progress_bar_satellite)

    @property
    def progress_bar_satellite_label(self):
        return self.selenium.find_element(*self._progress_bar_satellite_label)

    @property
    def progress_bar_rhv(self):
        return self.selenium.find_element(*self._progress_bar_rhv)

    @property
    def progress_bar_rhv_label(self):
        return self.selenium.find_element(*self._progress_bar_rhv_label)

    @property
    def progress_bar_cloudforms(self):
        return self.selenium.find_element(*self._progress_bar_cloudforms)

    @property
    def progress_bar_cloudforms_label(self):
        return self.selenium.find_element(*self._progress_bar_cloudforms_label)

    @property
    def progress_bar_openshift(self):
        return self.selenium.find_element(*self._progress_bar_openshift)

    @property
    def progress_bar_openshift_label(self):
        return self.selenium.find_element(*self._progress_bar_openshift_label)

    @property
    def progress_bar_openstack(self):
        return self.selenium.find_element(*self._progress_bar_openstack)

    @property
    def progress_bar_openstack_label(self):
        return self.selenium.find_element(*self._progress_bar_openstack_label)

    @property
    def logs_dropdown(self):
        return Select(self.selenium.find_element(*self._logs_dropdown_loc))

    @property
    def content_error_container(self):
        return self.selenium.find_element(*self._content_error_container)

    @property
    def abandon_button(self):
        return self.selenium.find_element(*self._abandon_button)

    @property
    def abandon_delete_button(self):
        return self.selenium.find_element(*self._abandon_delete_button)

    @property
    def redeploy_button(self):
        return self.selenium.find_element(*self._redeploy_button)

    # actions

    def click_overview_tab(self):
        return self.overview_tab.click()

    def click_details_tab(self):
        return self.details_tab.click()

    def click_log_tab(self):
        return self.log_tab.click()

    def view_log(self, log_file):
        """
        Select log to view from dropdown. Valid choices:
            foreman_log, fusor_log, candlepin_log,
            ansible_log, messages_log
        """
        self.click_log_tab()
        self.logs_dropdown.select_by_value(log_file)

    def deployment_complete(self):
        """
        Iterate through all of the progress bars on the page and return true if there is an error
        or all are successful
        """
        all_success = True
        error_found = False

        for progress_bar in self.progress_bar_all:
            if not self.progress_bar_success(progress_bar):
                all_success = False

            if self.progress_bar_error(progress_bar):
                error_found = True

        return error_found or all_success

    def deployment_result(self):
        """
        Check the result of all products being deployed.
        Return True if deployment was successful, False otherwise
        """
        # If there is a Content Sync error there will be no progress bars visible
        # Don't default to success if there are no progress bars present
        result = len(self.progress_bar_all) > 0
        for progress_bar in self.progress_bar_all:
            if not self.progress_bar_success(progress_bar):
                result = False

        return result

    def progress_bar_success(self, progress_bar):
        return self._progress_bar_class_success_name in progress_bar.get_attribute('class')

    def progress_bar_error(self, progress_bar):
        return self._progress_bar_class_error_name in progress_bar.get_attribute('class')

    def progress_bar_waiting(self, progress_bar):
        return (not (self.progress_bar_success(progress_bar) or self.progress_bar_error(progress_bar)) and
                (int(progress_bar.get_attribute('aria-valuemin')) == int(progress_bar.get_attribute('aria-valuenow'))))

    def progress_bar_processing(self, progress_bar):
        return (not (self.progress_bar_success(progress_bar) or self.progress_bar_error(progress_bar)) and
                (int(progress_bar.get_attribute('aria-valuemin')) < int(progress_bar.get_attribute('aria-valuenow')) < int(progress_bar.get_attribute('aria-valuemax'))))

    ############################################################################
    # Content Error Actions
    ############################################################################
    def has_content_error(self):
        """
        Return True if installation progress shows that a content error occurred
        """
        result = True
        try:
            # Exception thrown if content error property doesn't exist
            self.content_error_container.is_displayed()
        except:
            result = False

        return result

    def click_abandon_button(self):
        return self.abandon_button.click()

    def click_abandon_delete_button(self):
        return self.abandon_delete_button.click()

    def click_redeploy_button(self):
        return self.redeploy_button.click()
