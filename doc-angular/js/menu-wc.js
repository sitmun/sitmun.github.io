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
                    <a href="index.html" data-type="index-link">SITMUN Core Angular Library documentation</a>
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
                                <a href="modules/AngularHalModule.html" data-type="entity-link">AngularHalModule</a>
                                <li class="chapter inner">
                                    <div class="simple menu-toggler" data-toggle="collapse" ${ isNormalMode ?
                                        'data-target="#injectables-links-module-AngularHalModule-a9b78c45961283e4ede586f38b6d3cf6"' : 'data-target="#xs-injectables-links-module-AngularHalModule-a9b78c45961283e4ede586f38b6d3cf6"' }>
                                        <span class="icon ion-md-arrow-round-down"></span>
                                        <span>Injectables</span>
                                        <span class="icon ion-ios-arrow-down"></span>
                                    </div>
                                    <ul class="links collapse" ${ isNormalMode ? 'id="injectables-links-module-AngularHalModule-a9b78c45961283e4ede586f38b6d3cf6"' :
                                        'id="xs-injectables-links-module-AngularHalModule-a9b78c45961283e4ede586f38b6d3cf6"' }>
                                        <li class="link">
                                            <a href="injectables/ExternalService.html"
                                                data-type="entity-link" data-context="sub-entity" data-context-id="modules" }>ExternalService</a>
                                        </li>
                                    </ul>
                                </li>
                            </li>
                            <li class="link">
                                <a href="modules/AppModule.html" data-type="entity-link">AppModule</a>
                                    <li class="chapter inner">
                                        <div class="simple menu-toggler" data-toggle="collapse" ${ isNormalMode ?
                                            'data-target="#components-links-module-AppModule-b282a607dfc440a749b603e50eb66307"' : 'data-target="#xs-components-links-module-AppModule-b282a607dfc440a749b603e50eb66307"' }>
                                            <span class="icon ion-md-cog"></span>
                                            <span>Components</span>
                                            <span class="icon ion-ios-arrow-down"></span>
                                        </div>
                                        <ul class="links collapse" ${ isNormalMode ? 'id="components-links-module-AppModule-b282a607dfc440a749b603e50eb66307"' :
                                            'id="xs-components-links-module-AppModule-b282a607dfc440a749b603e50eb66307"' }>
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
                                <a href="modules/SitmunFrontendCoreModule.html" data-type="entity-link">SitmunFrontendCoreModule</a>
                                <li class="chapter inner">
                                    <div class="simple menu-toggler" data-toggle="collapse" ${ isNormalMode ?
                                        'data-target="#directives-links-module-SitmunFrontendCoreModule-689327e49f3a3ebb35284f190e0ac10a"' : 'data-target="#xs-directives-links-module-SitmunFrontendCoreModule-689327e49f3a3ebb35284f190e0ac10a"' }>
                                        <span class="icon ion-md-code-working"></span>
                                        <span>Directives</span>
                                        <span class="icon ion-ios-arrow-down"></span>
                                    </div>
                                    <ul class="links collapse" ${ isNormalMode ? 'id="directives-links-module-SitmunFrontendCoreModule-689327e49f3a3ebb35284f190e0ac10a"' :
                                        'id="xs-directives-links-module-SitmunFrontendCoreModule-689327e49f3a3ebb35284f190e0ac10a"' }>
                                        <li class="link">
                                            <a href="directives/HasAnyAuthorityDirective.html"
                                                data-type="entity-link" data-context="sub-entity" data-context-id="modules">HasAnyAuthorityDirective</a>
                                        </li>
                                        <li class="link">
                                            <a href="directives/HasAnyAuthorityOnTerritoryDirective.html"
                                                data-type="entity-link" data-context="sub-entity" data-context-id="modules">HasAnyAuthorityOnTerritoryDirective</a>
                                        </li>
                                    </ul>
                                </li>
                                <li class="chapter inner">
                                    <div class="simple menu-toggler" data-toggle="collapse" ${ isNormalMode ?
                                        'data-target="#injectables-links-module-SitmunFrontendCoreModule-689327e49f3a3ebb35284f190e0ac10a"' : 'data-target="#xs-injectables-links-module-SitmunFrontendCoreModule-689327e49f3a3ebb35284f190e0ac10a"' }>
                                        <span class="icon ion-md-arrow-round-down"></span>
                                        <span>Injectables</span>
                                        <span class="icon ion-ios-arrow-down"></span>
                                    </div>
                                    <ul class="links collapse" ${ isNormalMode ? 'id="injectables-links-module-SitmunFrontendCoreModule-689327e49f3a3ebb35284f190e0ac10a"' :
                                        'id="xs-injectables-links-module-SitmunFrontendCoreModule-689327e49f3a3ebb35284f190e0ac10a"' }>
                                        <li class="link">
                                            <a href="injectables/Principal.html"
                                                data-type="entity-link" data-context="sub-entity" data-context-id="modules" }>Principal</a>
                                        </li>
                                    </ul>
                                </li>
                            </li>
                            <li class="link">
                                <a href="modules/SitmunPluginCoreModule.html" data-type="entity-link">SitmunPluginCoreModule</a>
                                    <li class="chapter inner">
                                        <div class="simple menu-toggler" data-toggle="collapse" ${ isNormalMode ?
                                            'data-target="#components-links-module-SitmunPluginCoreModule-d625fba2888a7de2b828a7ae70fc7325"' : 'data-target="#xs-components-links-module-SitmunPluginCoreModule-d625fba2888a7de2b828a7ae70fc7325"' }>
                                            <span class="icon ion-md-cog"></span>
                                            <span>Components</span>
                                            <span class="icon ion-ios-arrow-down"></span>
                                        </div>
                                        <ul class="links collapse" ${ isNormalMode ? 'id="components-links-module-SitmunPluginCoreModule-d625fba2888a7de2b828a7ae70fc7325"' :
                                            'id="xs-components-links-module-SitmunPluginCoreModule-d625fba2888a7de2b828a7ae70fc7325"' }>
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
                                <a href="classes/Application.html" data-type="entity-link">Application</a>
                            </li>
                            <li class="link">
                                <a href="classes/ApplicationBackground.html" data-type="entity-link">ApplicationBackground</a>
                            </li>
                            <li class="link">
                                <a href="classes/ApplicationParameter.html" data-type="entity-link">ApplicationParameter</a>
                            </li>
                            <li class="link">
                                <a href="classes/AppPage.html" data-type="entity-link">AppPage</a>
                            </li>
                            <li class="link">
                                <a href="classes/AuthInterceptor.html" data-type="entity-link">AuthInterceptor</a>
                            </li>
                            <li class="link">
                                <a href="classes/Background.html" data-type="entity-link">Background</a>
                            </li>
                            <li class="link">
                                <a href="classes/BaseLayerGroup.html" data-type="entity-link">BaseLayerGroup</a>
                            </li>
                            <li class="link">
                                <a href="classes/Cartography.html" data-type="entity-link">Cartography</a>
                            </li>
                            <li class="link">
                                <a href="classes/CartographyAvailability.html" data-type="entity-link">CartographyAvailability</a>
                            </li>
                            <li class="link">
                                <a href="classes/CartographyGroup.html" data-type="entity-link">CartographyGroup</a>
                            </li>
                            <li class="link">
                                <a href="classes/Connection.html" data-type="entity-link">Connection</a>
                            </li>
                            <li class="link">
                                <a href="classes/FeatureInfoDialogData.html" data-type="entity-link">FeatureInfoDialogData</a>
                            </li>
                            <li class="link">
                                <a href="classes/FeatureInfoRequestData.html" data-type="entity-link">FeatureInfoRequestData</a>
                            </li>
                            <li class="link">
                                <a href="classes/Layer.html" data-type="entity-link">Layer</a>
                            </li>
                            <li class="link">
                                <a href="classes/LayerConfiguration.html" data-type="entity-link">LayerConfiguration</a>
                            </li>
                            <li class="link">
                                <a href="classes/LayerGroup.html" data-type="entity-link">LayerGroup</a>
                            </li>
                            <li class="link">
                                <a href="classes/LayerSelectionDialogData.html" data-type="entity-link">LayerSelectionDialogData</a>
                            </li>
                            <li class="link">
                                <a href="classes/MapComponentStatus.html" data-type="entity-link">MapComponentStatus</a>
                            </li>
                            <li class="link">
                                <a href="classes/MapConfiguration.html" data-type="entity-link">MapConfiguration</a>
                            </li>
                            <li class="link">
                                <a href="classes/MapOptions.html" data-type="entity-link">MapOptions</a>
                            </li>
                            <li class="link">
                                <a href="classes/MapOptionsConfiguration.html" data-type="entity-link">MapOptionsConfiguration</a>
                            </li>
                            <li class="link">
                                <a href="classes/OptionalParameter.html" data-type="entity-link">OptionalParameter</a>
                            </li>
                            <li class="link">
                                <a href="classes/ResourceArray.html" data-type="entity-link">ResourceArray</a>
                            </li>
                            <li class="link">
                                <a href="classes/ResourceHelper.html" data-type="entity-link">ResourceHelper</a>
                            </li>
                            <li class="link">
                                <a href="classes/RestService.html" data-type="entity-link">RestService</a>
                            </li>
                            <li class="link">
                                <a href="classes/Role.html" data-type="entity-link">Role</a>
                            </li>
                            <li class="link">
                                <a href="classes/Service.html" data-type="entity-link">Service</a>
                            </li>
                            <li class="link">
                                <a href="classes/ServiceParameter.html" data-type="entity-link">ServiceParameter</a>
                            </li>
                            <li class="link">
                                <a href="classes/Task.html" data-type="entity-link">Task</a>
                            </li>
                            <li class="link">
                                <a href="classes/TaskAvailability.html" data-type="entity-link">TaskAvailability</a>
                            </li>
                            <li class="link">
                                <a href="classes/TaskGroup.html" data-type="entity-link">TaskGroup</a>
                            </li>
                            <li class="link">
                                <a href="classes/TaskParameter.html" data-type="entity-link">TaskParameter</a>
                            </li>
                            <li class="link">
                                <a href="classes/TaskType.html" data-type="entity-link">TaskType</a>
                            </li>
                            <li class="link">
                                <a href="classes/TaskUI.html" data-type="entity-link">TaskUI</a>
                            </li>
                            <li class="link">
                                <a href="classes/Territory.html" data-type="entity-link">Territory</a>
                            </li>
                            <li class="link">
                                <a href="classes/TerritoryType.html" data-type="entity-link">TerritoryType</a>
                            </li>
                            <li class="link">
                                <a href="classes/Tree.html" data-type="entity-link">Tree</a>
                            </li>
                            <li class="link">
                                <a href="classes/TreeNode.html" data-type="entity-link">TreeNode</a>
                            </li>
                            <li class="link">
                                <a href="classes/User.html" data-type="entity-link">User</a>
                            </li>
                            <li class="link">
                                <a href="classes/UserConfiguration.html" data-type="entity-link">UserConfiguration</a>
                            </li>
                            <li class="link">
                                <a href="classes/UserPosition.html" data-type="entity-link">UserPosition</a>
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
                                    <a href="injectables/AccountService.html" data-type="entity-link">AccountService</a>
                                </li>
                                <li class="link">
                                    <a href="injectables/ApplicationBackgroundService.html" data-type="entity-link">ApplicationBackgroundService</a>
                                </li>
                                <li class="link">
                                    <a href="injectables/ApplicationParameterService.html" data-type="entity-link">ApplicationParameterService</a>
                                </li>
                                <li class="link">
                                    <a href="injectables/ApplicationService.html" data-type="entity-link">ApplicationService</a>
                                </li>
                                <li class="link">
                                    <a href="injectables/AuthService.html" data-type="entity-link">AuthService</a>
                                </li>
                                <li class="link">
                                    <a href="injectables/BackgroundService.html" data-type="entity-link">BackgroundService</a>
                                </li>
                                <li class="link">
                                    <a href="injectables/CartographyAvailabilityService.html" data-type="entity-link">CartographyAvailabilityService</a>
                                </li>
                                <li class="link">
                                    <a href="injectables/CartographyGroupService.html" data-type="entity-link">CartographyGroupService</a>
                                </li>
                                <li class="link">
                                    <a href="injectables/CartographyService.html" data-type="entity-link">CartographyService</a>
                                </li>
                                <li class="link">
                                    <a href="injectables/ConnectionService.html" data-type="entity-link">ConnectionService</a>
                                </li>
                                <li class="link">
                                    <a href="injectables/ExternalConfigurationService.html" data-type="entity-link">ExternalConfigurationService</a>
                                </li>
                                <li class="link">
                                    <a href="injectables/LoginService.html" data-type="entity-link">LoginService</a>
                                </li>
                                <li class="link">
                                    <a href="injectables/LoginService-1.html" data-type="entity-link">LoginService</a>
                                </li>
                                <li class="link">
                                    <a href="injectables/MapConfigurationManagerService.html" data-type="entity-link">MapConfigurationManagerService</a>
                                </li>
                                <li class="link">
                                    <a href="injectables/MatPaginationIntlService.html" data-type="entity-link">MatPaginationIntlService</a>
                                </li>
                                <li class="link">
                                    <a href="injectables/Resource.html" data-type="entity-link">Resource</a>
                                </li>
                                <li class="link">
                                    <a href="injectables/ResourceService.html" data-type="entity-link">ResourceService</a>
                                </li>
                                <li class="link">
                                    <a href="injectables/RoleService.html" data-type="entity-link">RoleService</a>
                                </li>
                                <li class="link">
                                    <a href="injectables/ServiceParameterService.html" data-type="entity-link">ServiceParameterService</a>
                                </li>
                                <li class="link">
                                    <a href="injectables/ServiceService.html" data-type="entity-link">ServiceService</a>
                                </li>
                                <li class="link">
                                    <a href="injectables/TaskAvailabilityService.html" data-type="entity-link">TaskAvailabilityService</a>
                                </li>
                                <li class="link">
                                    <a href="injectables/TaskGroupService.html" data-type="entity-link">TaskGroupService</a>
                                </li>
                                <li class="link">
                                    <a href="injectables/TaskParameterService.html" data-type="entity-link">TaskParameterService</a>
                                </li>
                                <li class="link">
                                    <a href="injectables/TaskService.html" data-type="entity-link">TaskService</a>
                                </li>
                                <li class="link">
                                    <a href="injectables/TaskTypeService.html" data-type="entity-link">TaskTypeService</a>
                                </li>
                                <li class="link">
                                    <a href="injectables/TaskUIService.html" data-type="entity-link">TaskUIService</a>
                                </li>
                                <li class="link">
                                    <a href="injectables/TerritoryService.html" data-type="entity-link">TerritoryService</a>
                                </li>
                                <li class="link">
                                    <a href="injectables/TerritoryTypeService.html" data-type="entity-link">TerritoryTypeService</a>
                                </li>
                                <li class="link">
                                    <a href="injectables/TreeNodeService.html" data-type="entity-link">TreeNodeService</a>
                                </li>
                                <li class="link">
                                    <a href="injectables/TreeService.html" data-type="entity-link">TreeService</a>
                                </li>
                                <li class="link">
                                    <a href="injectables/UserConfigurationService.html" data-type="entity-link">UserConfigurationService</a>
                                </li>
                                <li class="link">
                                    <a href="injectables/UserPositionService.html" data-type="entity-link">UserPositionService</a>
                                </li>
                                <li class="link">
                                    <a href="injectables/UserService.html" data-type="entity-link">UserService</a>
                                </li>
                            </ul>
                        </li>
                    <li class="chapter">
                        <div class="simple menu-toggler" data-toggle="collapse" ${ isNormalMode ? 'data-target="#interceptors-links"' :
                            'data-target="#xs-interceptors-links"' }>
                            <span class="icon ion-ios-swap"></span>
                            <span>Interceptors</span>
                            <span class="icon ion-ios-arrow-down"></span>
                        </div>
                        <ul class="links collapse " ${ isNormalMode ? 'id="interceptors-links"' : 'id="xs-interceptors-links"' }>
                            <li class="link">
                                <a href="interceptors/AuthExpiredInterceptor.html" data-type="entity-link">AuthExpiredInterceptor</a>
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
                                <a href="interfaces/ArrayInterface.html" data-type="entity-link">ArrayInterface</a>
                            </li>
                            <li class="link">
                                <a href="interfaces/ExternalConfiguration.html" data-type="entity-link">ExternalConfiguration</a>
                            </li>
                            <li class="link">
                                <a href="interfaces/ExternalConfigurationHandlerInterface.html" data-type="entity-link">ExternalConfigurationHandlerInterface</a>
                            </li>
                            <li class="link">
                                <a href="interfaces/InfoDialogData.html" data-type="entity-link">InfoDialogData</a>
                            </li>
                            <li class="link">
                                <a href="interfaces/Sort.html" data-type="entity-link">Sort</a>
                            </li>
                            <li class="link">
                                <a href="interfaces/SubTypeBuilder.html" data-type="entity-link">SubTypeBuilder</a>
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
                                <a href="miscellaneous/typealiases.html" data-type="entity-link">Type aliases</a>
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