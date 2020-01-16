'use strict';


customElements.define('compodoc-menu', class extends HTMLElement {
    constructor() {
        super();
        this.isNormalMode = this.getAttribute('mode') === 'normal';
    }

    connectedCallback() {
        this.render(this.isNormalMode);
    }

    render(isNormalMode) {
        let tp = lithtml.html(`
        <nav>
            <ul class="list">
                <li class="title">
                    <a href="index.html" data-type="index-link">SITMUN Frontend GUI Angular Library documentation</a>
                </li>

                <li class="divider"></li>
                ${ isNormalMode ? `<div id="book-search-input" role="search"><input type="text" placeholder="Type to search"></div>` : '' }
                <li class="chapter">
                    <a data-type="chapter-link" href="index.html"><span class="icon ion-ios-home"></span>Getting started</a>
                    <ul class="links">
                        <li class="link">
                            <a href="overview.html" data-type="chapter-link">
                                <span class="icon ion-ios-keypad"></span>Overview
                            </a>
                        </li>
                        <li class="link">
                            <a href="index.html" data-type="chapter-link">
                                <span class="icon ion-ios-paper"></span>README
                            </a>
                        </li>
                        <li class="link">
                            <a href="license.html"  data-type="chapter-link">
                                <span class="icon ion-ios-paper"></span>LICENSE
                            </a>
                        </li>
                                <li class="link">
                                    <a href="dependencies.html" data-type="chapter-link">
                                        <span class="icon ion-ios-list"></span>Dependencies
                                    </a>
                                </li>
                    </ul>
                </li>
                    <li class="chapter additional">
                        <div class="simple menu-toggler" data-toggle="collapse" ${ isNormalMode ? 'data-target="#additional-pages"'
                            : 'data-target="#xs-additional-pages"' }>
                            <span class="icon ion-ios-book"></span>
                            <span>Additional documentation</span>
                            <span class="icon ion-ios-arrow-down"></span>
                        </div>
                        <ul class="links collapse " ${ isNormalMode ? 'id="additional-pages"' : 'id="xs-additional-pages"' }>
                                    <li class="link ">
                                        <a href="additional-documentation/usage.html" data-type="entity-link" data-context-id="additional">USAGE</a>
                                    </li>
                        </ul>
                    </li>
                    <li class="chapter modules">
                        <a data-type="chapter-link" href="modules.html">
                            <div class="menu-toggler linked" data-toggle="collapse" ${ isNormalMode ?
                                'data-target="#modules-links"' : 'data-target="#xs-modules-links"' }>
                                <span class="icon ion-ios-archive"></span>
                                <span class="link-name">Modules</span>
                                <span class="icon ion-ios-arrow-down"></span>
                            </div>
                        </a>
                        <ul class="links collapse " ${ isNormalMode ? 'id="modules-links"' : 'id="xs-modules-links"' }>
                            <li class="link">
                                <a href="modules/AppModule.html" data-type="entity-link">AppModule</a>
                                    <li class="chapter inner">
                                        <div class="simple menu-toggler" data-toggle="collapse" ${ isNormalMode ?
                                            'data-target="#components-links-module-AppModule-639bd03be059570700ae88d6cce8213d"' : 'data-target="#xs-components-links-module-AppModule-639bd03be059570700ae88d6cce8213d"' }>
                                            <span class="icon ion-md-cog"></span>
                                            <span>Components</span>
                                            <span class="icon ion-ios-arrow-down"></span>
                                        </div>
                                        <ul class="links collapse" ${ isNormalMode ? 'id="components-links-module-AppModule-639bd03be059570700ae88d6cce8213d"' :
                                            'id="xs-components-links-module-AppModule-639bd03be059570700ae88d6cce8213d"' }>
                                            <li class="link">
                                                <a href="components/AppComponent.html"
                                                    data-type="entity-link" data-context="sub-entity" data-context-id="modules">AppComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/HomeComponent.html"
                                                    data-type="entity-link" data-context="sub-entity" data-context-id="modules">HomeComponent</a>
                                            </li>
                                        </ul>
                                    </li>
                            </li>
                            <li class="link">
                                <a href="modules/SitmunFrontendGuiModule.html" data-type="entity-link">SitmunFrontendGuiModule</a>
                                    <li class="chapter inner">
                                        <div class="simple menu-toggler" data-toggle="collapse" ${ isNormalMode ?
                                            'data-target="#components-links-module-SitmunFrontendGuiModule-4b415abc51d0ac7a641b5fb30fccc567"' : 'data-target="#xs-components-links-module-SitmunFrontendGuiModule-4b415abc51d0ac7a641b5fb30fccc567"' }>
                                            <span class="icon ion-md-cog"></span>
                                            <span>Components</span>
                                            <span class="icon ion-ios-arrow-down"></span>
                                        </div>
                                        <ul class="links collapse" ${ isNormalMode ? 'id="components-links-module-SitmunFrontendGuiModule-4b415abc51d0ac7a641b5fb30fccc567"' :
                                            'id="xs-components-links-module-SitmunFrontendGuiModule-4b415abc51d0ac7a641b5fb30fccc567"' }>
                                            <li class="link">
                                                <a href="components/AccountChangePasswordComponent.html"
                                                    data-type="entity-link" data-context="sub-entity" data-context-id="modules">AccountChangePasswordComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/AccountEditComponent.html"
                                                    data-type="entity-link" data-context="sub-entity" data-context-id="modules">AccountEditComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/ApplicationBackgroundEditDialog.html"
                                                    data-type="entity-link" data-context="sub-entity" data-context-id="modules">ApplicationBackgroundEditDialog</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/ApplicationBackgroundListComponent.html"
                                                    data-type="entity-link" data-context="sub-entity" data-context-id="modules">ApplicationBackgroundListComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/ApplicationEditComponent.html"
                                                    data-type="entity-link" data-context="sub-entity" data-context-id="modules">ApplicationEditComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/ApplicationListComponent.html"
                                                    data-type="entity-link" data-context="sub-entity" data-context-id="modules">ApplicationListComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/ApplicationParameterEditDialog.html"
                                                    data-type="entity-link" data-context="sub-entity" data-context-id="modules">ApplicationParameterEditDialog</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/ApplicationParameterListComponent.html"
                                                    data-type="entity-link" data-context="sub-entity" data-context-id="modules">ApplicationParameterListComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/BackgroundEditComponent.html"
                                                    data-type="entity-link" data-context="sub-entity" data-context-id="modules">BackgroundEditComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/BackgroundListComponent.html"
                                                    data-type="entity-link" data-context="sub-entity" data-context-id="modules">BackgroundListComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/CartographyAvailabilityEditDialog.html"
                                                    data-type="entity-link" data-context="sub-entity" data-context-id="modules">CartographyAvailabilityEditDialog</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/CartographyAvailabilityListComponent.html"
                                                    data-type="entity-link" data-context="sub-entity" data-context-id="modules">CartographyAvailabilityListComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/CartographyEditComponent.html"
                                                    data-type="entity-link" data-context="sub-entity" data-context-id="modules">CartographyEditComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/CartographyGroupEditComponent.html"
                                                    data-type="entity-link" data-context="sub-entity" data-context-id="modules">CartographyGroupEditComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/CartographyGroupListComponent.html"
                                                    data-type="entity-link" data-context="sub-entity" data-context-id="modules">CartographyGroupListComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/CartographyListComponent.html"
                                                    data-type="entity-link" data-context="sub-entity" data-context-id="modules">CartographyListComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/ConnectionEditComponent.html"
                                                    data-type="entity-link" data-context="sub-entity" data-context-id="modules">ConnectionEditComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/ConnectionListComponent.html"
                                                    data-type="entity-link" data-context="sub-entity" data-context-id="modules">ConnectionListComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/FeatureInfoDialogComponent.html"
                                                    data-type="entity-link" data-context="sub-entity" data-context-id="modules">FeatureInfoDialogComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/LayerSelectionDialogComponent.html"
                                                    data-type="entity-link" data-context="sub-entity" data-context-id="modules">LayerSelectionDialogComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/LoginComponent.html"
                                                    data-type="entity-link" data-context="sub-entity" data-context-id="modules">LoginComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/MapComponent.html"
                                                    data-type="entity-link" data-context="sub-entity" data-context-id="modules">MapComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/MessageDialogComponent.html"
                                                    data-type="entity-link" data-context="sub-entity" data-context-id="modules">MessageDialogComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/RoleEditComponent.html"
                                                    data-type="entity-link" data-context="sub-entity" data-context-id="modules">RoleEditComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/RoleListComponent.html"
                                                    data-type="entity-link" data-context="sub-entity" data-context-id="modules">RoleListComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/ServiceEditComponent.html"
                                                    data-type="entity-link" data-context="sub-entity" data-context-id="modules">ServiceEditComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/ServiceListComponent.html"
                                                    data-type="entity-link" data-context="sub-entity" data-context-id="modules">ServiceListComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/ServiceParameterEditDialog.html"
                                                    data-type="entity-link" data-context="sub-entity" data-context-id="modules">ServiceParameterEditDialog</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/ServiceParameterListComponent.html"
                                                    data-type="entity-link" data-context="sub-entity" data-context-id="modules">ServiceParameterListComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/TaskAvailabilityEditDialog.html"
                                                    data-type="entity-link" data-context="sub-entity" data-context-id="modules">TaskAvailabilityEditDialog</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/TaskAvailabilityListComponent.html"
                                                    data-type="entity-link" data-context="sub-entity" data-context-id="modules">TaskAvailabilityListComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/TaskEditComponent.html"
                                                    data-type="entity-link" data-context="sub-entity" data-context-id="modules">TaskEditComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/TaskGroupEditComponent.html"
                                                    data-type="entity-link" data-context="sub-entity" data-context-id="modules">TaskGroupEditComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/TaskGroupListComponent.html"
                                                    data-type="entity-link" data-context="sub-entity" data-context-id="modules">TaskGroupListComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/TaskListComponent.html"
                                                    data-type="entity-link" data-context="sub-entity" data-context-id="modules">TaskListComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/TaskParameterEditDialog.html"
                                                    data-type="entity-link" data-context="sub-entity" data-context-id="modules">TaskParameterEditDialog</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/TaskParameterListComponent.html"
                                                    data-type="entity-link" data-context="sub-entity" data-context-id="modules">TaskParameterListComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/TaskTypeEditComponent.html"
                                                    data-type="entity-link" data-context="sub-entity" data-context-id="modules">TaskTypeEditComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/TaskTypeListComponent.html"
                                                    data-type="entity-link" data-context="sub-entity" data-context-id="modules">TaskTypeListComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/TaskUIEditComponent.html"
                                                    data-type="entity-link" data-context="sub-entity" data-context-id="modules">TaskUIEditComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/TaskUIListComponent.html"
                                                    data-type="entity-link" data-context="sub-entity" data-context-id="modules">TaskUIListComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/TerritoryEditComponent.html"
                                                    data-type="entity-link" data-context="sub-entity" data-context-id="modules">TerritoryEditComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/TerritoryListComponent.html"
                                                    data-type="entity-link" data-context="sub-entity" data-context-id="modules">TerritoryListComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/TerritoryTypeEditComponent.html"
                                                    data-type="entity-link" data-context="sub-entity" data-context-id="modules">TerritoryTypeEditComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/TerritoryTypeListComponent.html"
                                                    data-type="entity-link" data-context="sub-entity" data-context-id="modules">TerritoryTypeListComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/TreeEditComponent.html"
                                                    data-type="entity-link" data-context="sub-entity" data-context-id="modules">TreeEditComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/TreeListComponent.html"
                                                    data-type="entity-link" data-context="sub-entity" data-context-id="modules">TreeListComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/TreeNodeEditDialog.html"
                                                    data-type="entity-link" data-context="sub-entity" data-context-id="modules">TreeNodeEditDialog</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/TreeNodeListComponent.html"
                                                    data-type="entity-link" data-context="sub-entity" data-context-id="modules">TreeNodeListComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/UserChangePasswordComponent.html"
                                                    data-type="entity-link" data-context="sub-entity" data-context-id="modules">UserChangePasswordComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/UserConfigurationEditDialog.html"
                                                    data-type="entity-link" data-context="sub-entity" data-context-id="modules">UserConfigurationEditDialog</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/UserConfigurationListComponent.html"
                                                    data-type="entity-link" data-context="sub-entity" data-context-id="modules">UserConfigurationListComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/UserEditComponent.html"
                                                    data-type="entity-link" data-context="sub-entity" data-context-id="modules">UserEditComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/UserListComponent.html"
                                                    data-type="entity-link" data-context="sub-entity" data-context-id="modules">UserListComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/UserPositionEditDialog.html"
                                                    data-type="entity-link" data-context="sub-entity" data-context-id="modules">UserPositionEditDialog</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/UserPositionListComponent.html"
                                                    data-type="entity-link" data-context="sub-entity" data-context-id="modules">UserPositionListComponent</a>
                                            </li>
                                        </ul>
                                    </li>
                            </li>
                </ul>
                </li>
                    <li class="chapter">
                        <div class="simple menu-toggler" data-toggle="collapse" ${ isNormalMode ? 'data-target="#components-links"' :
                            'data-target="#xs-components-links"' }>
                            <span class="icon ion-md-cog"></span>
                            <span>Components</span>
                            <span class="icon ion-ios-arrow-down"></span>
                        </div>
                        <ul class="links collapse " ${ isNormalMode ? 'id="components-links"' : 'id="xs-components-links"' }>
                            <li class="link">
                                <a href="components/UserConfigurationEditComponent.html" data-type="entity-link">UserConfigurationEditComponent</a>
                            </li>
                            <li class="link">
                                <a href="components/UserPositionEditComponent.html" data-type="entity-link">UserPositionEditComponent</a>
                            </li>
                        </ul>
                    </li>
                    <li class="chapter">
                        <div class="simple menu-toggler" data-toggle="collapse" ${ isNormalMode ? 'data-target="#classes-links"' :
                            'data-target="#xs-classes-links"' }>
                            <span class="icon ion-ios-paper"></span>
                            <span>Classes</span>
                            <span class="icon ion-ios-arrow-down"></span>
                        </div>
                        <ul class="links collapse " ${ isNormalMode ? 'id="classes-links"' : 'id="xs-classes-links"' }>
                            <li class="link">
                                <a href="classes/AppPage.html" data-type="entity-link">AppPage</a>
                            </li>
                            <li class="link">
                                <a href="classes/BaseLayerGroup.html" data-type="entity-link">BaseLayerGroup</a>
                            </li>
                            <li class="link">
                                <a href="classes/FeatureInfoDialogData.html" data-type="entity-link">FeatureInfoDialogData</a>
                            </li>
                            <li class="link">
                                <a href="classes/FeatureInfoRequestData.html" data-type="entity-link">FeatureInfoRequestData</a>
                            </li>
                            <li class="link">
                                <a href="classes/LayerSelectionDialogData.html" data-type="entity-link">LayerSelectionDialogData</a>
                            </li>
                            <li class="link">
                                <a href="classes/MapConfiguration.html" data-type="entity-link">MapConfiguration</a>
                            </li>
                            <li class="link">
                                <a href="classes/MapOptions.html" data-type="entity-link">MapOptions</a>
                            </li>
                        </ul>
                    </li>
                        <li class="chapter">
                            <div class="simple menu-toggler" data-toggle="collapse" ${ isNormalMode ? 'data-target="#injectables-links"' :
                                'data-target="#xs-injectables-links"' }>
                                <span class="icon ion-md-arrow-round-down"></span>
                                <span>Injectables</span>
                                <span class="icon ion-ios-arrow-down"></span>
                            </div>
                            <ul class="links collapse " ${ isNormalMode ? 'id="injectables-links"' : 'id="xs-injectables-links"' }>
                                <li class="link">
                                    <a href="injectables/ExternalConfigurationService.html" data-type="entity-link">ExternalConfigurationService</a>
                                </li>
                                <li class="link">
                                    <a href="injectables/LoginService.html" data-type="entity-link">LoginService</a>
                                </li>
                                <li class="link">
                                    <a href="injectables/MatPaginationIntlService.html" data-type="entity-link">MatPaginationIntlService</a>
                                </li>
                            </ul>
                        </li>
                    <li class="chapter">
                        <div class="simple menu-toggler" data-toggle="collapse" ${ isNormalMode ? 'data-target="#interfaces-links"' :
                            'data-target="#xs-interfaces-links"' }>
                            <span class="icon ion-md-information-circle-outline"></span>
                            <span>Interfaces</span>
                            <span class="icon ion-ios-arrow-down"></span>
                        </div>
                        <ul class="links collapse " ${ isNormalMode ? ' id="interfaces-links"' : 'id="xs-interfaces-links"' }>
                            <li class="link">
                                <a href="interfaces/InfoDialogData.html" data-type="entity-link">InfoDialogData</a>
                            </li>
                        </ul>
                    </li>
                    <li class="chapter">
                        <div class="simple menu-toggler" data-toggle="collapse" ${ isNormalMode ? 'data-target="#miscellaneous-links"'
                            : 'data-target="#xs-miscellaneous-links"' }>
                            <span class="icon ion-ios-cube"></span>
                            <span>Miscellaneous</span>
                            <span class="icon ion-ios-arrow-down"></span>
                        </div>
                        <ul class="links collapse " ${ isNormalMode ? 'id="miscellaneous-links"' : 'id="xs-miscellaneous-links"' }>
                            <li class="link">
                                <a href="miscellaneous/functions.html" data-type="entity-link">Functions</a>
                            </li>
                            <li class="link">
                                <a href="miscellaneous/variables.html" data-type="entity-link">Variables</a>
                            </li>
                        </ul>
                    </li>
                    <li class="chapter">
                        <a data-type="chapter-link" href="coverage.html"><span class="icon ion-ios-stats"></span>Documentation coverage</a>
                    </li>
                    <li class="divider"></li>
                    <li class="copyright">
                        Documentation generated using <a href="https://compodoc.app/" target="_blank">
                            <img data-src="images/compodoc-vectorise.png" class="img-responsive" data-type="compodoc-logo">
                        </a>
                    </li>
            </ul>
        </nav>
        `);
        this.innerHTML = tp.strings;
    }
});